from fastapi import Depends, FastAPI
from fastapi.dependencies.cache import DependencyCacheScope
from fastapi.testclient import TestClient

app = FastAPI()

counter_holder = {"counter": 0}


async def dep_counter():
    counter_holder["counter"] += 1
    return counter_holder["counter"]


async def super_dep(count: int = Depends(dep_counter)):
    return count


async def super_dep_app_cache(count: int = Depends(dep_counter, use_cache=DependencyCacheScope.app)):
    return count


@app.get("/counter/")
async def get_counter(count: int = Depends(dep_counter)):
    return {"counter": count}


@app.get("/sub-counter/")
async def get_sub_counter(
    subcount: int = Depends(super_dep), count: int = Depends(dep_counter)
):
    return {"counter": count, "subcounter": subcount}


@app.get("/sub-counter-no-cache/")
async def get_sub_counter_no_cache(
    subcount: int = Depends(super_dep),
    count: int = Depends(dep_counter, use_cache=False),
):
    return {"counter": count, "subcounter": subcount}


@app.get("/sub-counter-app-cache-top-level/")
async def get_sub_counter_app_cache_direct(
    subcount: int = Depends(super_dep),
    count: int = Depends(dep_counter, use_cache=DependencyCacheScope.app),
):
    return {"counter": count, "subcounter": subcount}


@app.get("/sub-counter-app-cache-indirect/")
async def get_counter_app_cache_indirect(
    subcount: int = Depends(super_dep_app_cache),
    count: int = Depends(dep_counter),
):
    return {"counter": count, "subcounter": subcount}


@app.get("/counter-app-cache/")
async def get_counter_app_cache(
    subcount: int = Depends(super_dep, use_cache=DependencyCacheScope.app),
    count: int = Depends(dep_counter),
):
    return {"counter": count, "subcounter": subcount}


client = TestClient(app)


def test_normal_counter():
    counter_holder["counter"] = 0
    response = client.get("/counter/")
    assert response.status_code == 200, response.text
    assert response.json() == {"counter": 1}
    response = client.get("/counter/")
    assert response.status_code == 200, response.text
    assert response.json() == {"counter": 2}


def test_sub_counter():
    counter_holder["counter"] = 0
    response = client.get("/sub-counter/")
    assert response.status_code == 200, response.text
    assert response.json() == {"counter": 1, "subcounter": 1}
    response = client.get("/sub-counter/")
    assert response.status_code == 200, response.text
    assert response.json() == {"counter": 2, "subcounter": 2}


def test_sub_counter_no_cache():
    counter_holder["counter"] = 0
    response = client.get("/sub-counter-no-cache/")
    assert response.status_code == 200, response.text
    assert response.json() == {"counter": 2, "subcounter": 1}
    response = client.get("/sub-counter-no-cache/")
    assert response.status_code == 200, response.text
    assert response.json() == {"counter": 4, "subcounter": 3}


def test_sub_counter_app_cache_top_level():
    counter_holder["counter"] = 0
    with TestClient(app) as client:
        response = client.get("/sub-counter-app-cache-top-level/")
        assert response.status_code == 200, response.text
        assert response.json() == {"counter": 1, "subcounter": 1}
        response = client.get("/sub-counter-app-cache-top-level/")
        assert response.status_code == 200, response.text
        assert response.json() == {"counter": 1, "subcounter": 1}


def test_sub_counter_app_cache_indirect():
    counter_holder["counter"] = 0
    with TestClient(app) as client:
        response = client.get("/sub-counter-app-cache-indirect/")
        assert response.status_code == 200, response.text
        assert response.json() == {"counter": 1, "subcounter": 1}
        response = client.get("/sub-counter-app-cache-indirect/")
        assert response.status_code == 200, response.text
        assert response.json() == {"counter": 1, "subcounter": 1}


def test_counter_app_cache():
    counter_holder["counter"] = 0
    with TestClient(app) as client:
        response = client.get("/counter-app-cache/")
        assert response.status_code == 200, response.text
        assert response.json() == {"counter": 1, "subcounter": 1}
        response = client.get("/counter-app-cache/")
        assert response.status_code == 200, response.text
        assert response.json() == {"counter": 2, "subcounter": 1}

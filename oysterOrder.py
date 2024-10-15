from fastapi import APIRouter, FastAPI

# Create a new router
router = APIRouter()

# Define a new endpoint
@router.get("/")
async def new_endpoint():
    return {"message": "Hello, this is a new oyster order!"}

# Create the FastAPI app
app = FastAPI()

# Include the router in the app
app.include_router(router)
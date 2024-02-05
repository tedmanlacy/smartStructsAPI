# İlk Adımlar

En basit FastAPI dosyası şu şekilde görünür:

```Python
{!../../../docs_src/first_steps/tutorial001.py!}
```

Yukarıda ki içeriği bir `main.py` dosyasına kopyalayın.

Uygulamayı çalıştırın:

<div class="termy">

```console
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
<span style="color: green;">INFO</span>:     Started reloader process [28720]
<span style="color: green;">INFO</span>:     Started server process [28722]
<span style="color: green;">INFO</span>:     Waiting for application startup.
<span style="color: green;">INFO</span>:     Application startup complete.
```

</div>

!!! note
    `uvicorn main:app` komutu şunu ifade eder:

    * `main`: `main.py` dosyası (Python "modülü").
    * `app`: `main.py` dosyası içerisinde `app = FastAPI()` satırıyla oluşturulan nesne.
    * `--reload`: Kod içerisinde değişiklik yapıldığında sunucunun yeniden başlatılmasını sağlar. Yalnızca geliştirme aşamasında kullanın.

Çıktı olarak şöyle bir satır göreceksiniz:

```hl_lines="4"
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Bu satır, yerel makinenizde uygulamanızın çalıştığı bağlantıyı gösterir.

### Kontrol Edelim

Tarayıcınızı açıp <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a> bağlantısına gidin.

Şu lekilde bir JSON yanıtı göreceksiniz:

```JSON
{"message": "Hello World"}
```

### Etkileşimli API Dokümantasyonu

Şimdi <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> bağlantısını açalım.

<a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a> tarafından sağlanan otomatik etkileşimli bir API dokümantasyonu göreceğiz:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternatif API Dokümantasyonu

Şimdi <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> bağlantısını açalım.

<a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a> tarafından sağlanan otomatik dokümantasyonu göreceğiz:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

### OpenAPI

**FastAPI**, **OpenAPI** standardını kullanarak tüm API'ınızın tamamını tanımlayan bir "şema" oluşturur.

#### "Şema"

"Şema", bir şeyin tanımı veya açıklamasıdır. Geliştirilen koddan ziyade soyut bir açıklamadır.

#### API "Şemaları"

Bu durumda, <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a>, API şemasını nasıl tanımlayacağınızı belirten şartnamedir.

Bu şema tanımı, API yollarınızla birlikte aldıkları olası parametreleri gibi tanımlamaları içerir.

#### Veri "Şeması"

"Şema" terimi, JSON içeriği gibi bazı verilerin şeklini de ifade edebilir.

Bu durumda, JSON özellikleri ve sahip oldukları veri türleri gibi anlamına gelir.

#### OpenAPI ve JSON Şema

OpenAPI, API'niz için bir API şeması tanımlar. Ve bu şema, JSON veri şemaları standardı olan **JSON Şema** kullanılarak API'niz tarafından gönderilen ve alınan verilerin tanımlarını (veya "şemalarını") içerir.

#### `openapi.json` kontrol et

OpenAPI şemasının nasıl göründüğünü merak ediyorsanız, FastAPI otomatik olarak tüm API'ınızın tanımlamalarını içeren bir JSON (şema) oluşturur.

Doğrudan şu bağlantıda görebilirsiniz: <a href="http://127.0.0.1:8000/openapi.json" class="external-link" target="_blank">http://127.0.0.1:8000/openapi.json</a>.

Aşağıdaki gibi başlayan bir JSON ile karşılaşacaksınız:

```JSON
{
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {



...
```

#### OpenAPI Amacı Nedir?

OpenAPI şeması, dahili olarak bulunan iki etkileşimli dokümantasyon sistemine güç veren şeydir.

Ve tamamen OpenAPI'ye dayalı düzinelerce alternatif vardır. **FastAPI** ile oluşturulmuş uygulamanıza bu alternatiflerden herhangi birini kolayca ekleyebilirsiniz.

API'nizle iletişim kuran istemciler için otomatik olarak kod oluşturmak için de kullanabilirsiniz. Örneğin, frontend, mobil veya IoT uygulamaları.

## Adım adım özet

### Adım 1: `FastAPI`yi içe aktarın

```Python hl_lines="1"
{!../../../docs_src/first_steps/tutorial001.py!}
```

`FastAPI`, API'niz için tüm fonksiyonları sağlayan bir Python sınıfıdır.

!!! note "Teknik Detaylar"
    `FastAPI` doğrudan `Starlette` kalıtım alan bir sınıftır.

    Tüm <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> fonksiyonlarını `FastAPI` ile de kullanabilirsiniz.

### Adım 2: Bir `FastAPI` örneği oluşturun

```Python hl_lines="3"
{!../../../docs_src/first_steps/tutorial001.py!}
```

Burada `app` değişkeni `FastAPI` sınıfının bir örneği olacaktır.

Bu tüm API'yi oluşturmak için ana etkileşim noktası olacaktır.

`uvicorn` komutunda atıfta bulunulan `app` ile aynıdır.

<div class="termy">

```console
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

Uygulamanızı aşağıdaki gibi oluşturursanız:

```Python hl_lines="3"
{!../../../docs_src/first_steps/tutorial002.py!}
```

Ve bunu `main.py` dosyasına koyduktan sonra `uvicorn` komutunu şu şekilde çağırabilirsiniz:

<div class="termy">

```console
$ uvicorn main:my_awesome_api --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

### Adım 3: *Path işlemleri* oluşturmak

#### Path

Burada "Path" URL'de ilk "\" ile başlayan son bölümü ifade eder.

Yani, şu şekilde bir URL'de:

```
https://example.com/items/foo
```

... path şöyle olabilir:

```
/items/foo
```

!!! info
    Genellikle bir "path", "endpoint" veya "route" olarak adlandırılabilir.

Bir API oluştururken, "path", "resource" ile "concern" ayırmanın ana yoludur.

#### İşlemler

Burada "işlem" HTTP methodlarından birini ifade eder.

Onlardan biri:

* `POST`
* `GET`
* `PUT`
* `DELETE`

... ve daha egzotik olanları:

* `OPTIONS`
* `HEAD`
* `PATCH`
* `TRACE`

HTTP protokolünde, bu "methodlardan" birini (veya daha fazlasını) kullanarak her path ile iletişim kurabilirsiniz.

---

API'lerinizi oluştururkan, belirli bir işlemi gerçekleştirirken belirli HTTP methodlarını kullanırsınız.

Normalde kullanılan:

* `POST`: veri oluşturmak.
* `GET`: veri okumak.
* `PUT`: veriyi güncellemek.
* `DELETE`: veriyi silmek.

Bu nedenle, OpenAPI'de HTTP methodlarından her birine "işlem" denir.

Bizde onlara "**işlemler**" diyeceğiz.

#### Bir *Path işlem decoratorleri* tanımlanmak

```Python hl_lines="6"
{!../../../docs_src/first_steps/tutorial001.py!}
```

`@app.get("/")` **FastAPI'ye** aşağıdaki fonksiyonun adresine giden istekleri işlemekten sorumlu olduğunu söyler:

* path `/`
* <abbr title="an HTTP GET method"><code>get</code> işlemi</abbr> kullanılarak


!!! info "`@decorator` Bilgisi"
    Python `@something` şeklinde ifadeleri "decorator" olarak adlandırır.

    Decoratoru bir fonksiyonun üzerine koyarsınız. Dekoratif bir şapka gibi (Sanırım terim buradan gelmektedir).

    Bir "decorator" fonksiyonu alır ve bazı işlemler gerçekleştir.

    Bizim durumumzda decarator **FastAPI'ye** fonksiyonun bir `get` işlemi ile `/` pathine geldiğini söyler.

    Bu **path işlem decoratordür**

Ayrıca diğer işlemleri de kullanabilirsiniz:

* `@app.post()`
* `@app.put()`
* `@app.delete()`

Ve daha egzotik olanları:

* `@app.options()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`

!!! tip
    Her işlemi (HTTP method) istediğiniz gibi kullanmakta özgürsünüz.

    **FastAPI** herhangi bir özel anlamı zorlamaz.

    Buradaki bilgiler bir gereklilik değil, bir kılavuz olarak sunulmaktadır.

    Örneğin, GraphQL kullanırkan normalde tüm işlemleri yalnızca `POST` işlemini kullanarak gerçekleştirirsiniz.

### Adım 4: **path işlem fonksiyonunu** tanımlayın

Aşağıdakiler bizim **path işlem fonksiyonlarımızdır**:

* **path**: `/`
* **işlem**: `get`
* **function**: "decorator"ün altındaki fonksiyondur (`@app.get("/")` altında).

```Python hl_lines="7"
{!../../../docs_src/first_steps/tutorial001.py!}
```

Bu bir Python fonksiyonudur.

Bir `GET` işlemi kullanarak "`/`" URL'sine bir istek geldiğinde **FastAPI** tarafından çağrılır.

Bu durumda bir `async` fonksiyonudur.

---

Bunu `async def` yerine normal bir fonksiyon olarakta tanımlayabilirsiniz.

```Python hl_lines="7"
{!../../../docs_src/first_steps/tutorial003.py!}
```

!!! note

    Eğer farkı bilmiyorsanız, [Async: *"Acelesi var?"*](../async.md#in-a-hurry){.internal-link target=_blank} kontrol edebilirsiniz.

### Adım 5: İçeriği geri döndürün


```Python hl_lines="8"
{!../../../docs_src/first_steps/tutorial001.py!}
```

Bir `dict`, `list` döndürebilir veya `str`, `int` gibi tekil değerler döndürebilirsiniz.

Ayrıca, Pydantic modellerini de döndürebilirsiniz. (Bununla ilgili daha sonra ayrıntılı bilgi göreceksiniz.)

Otomatik olarak JSON'a dönüştürülecek(ORM'ler vb. dahil) başka birçok nesne ve model vardır. En beğendiklerinizi kullanmayı deneyin, yüksek ihtimalle destekleniyordur.

## Özet

* `FastAPI`'yi içe aktarın.
* Bir `app` örneği oluşturun.
* **path işlem decorator** yazın. (`@app.get("/")` gibi)
* **path işlem fonksiyonu** yazın. (`def root(): ...` gibi)
* Development sunucunuzu çalıştırın. (`uvicorn main:app --reload` gibi)
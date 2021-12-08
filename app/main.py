import fastapi

app = fastapi.Fastapi()


@app.get()
def hello():
    return {
        "hello": "app"
    }
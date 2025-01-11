from fastapi import FastAPI

app = FastAPI()


@app.get("/closeapp")
def close_app():
    return {"message": "Hello from FastAPI"}, print("success")

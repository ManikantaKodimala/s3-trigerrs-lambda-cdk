from fastapi import FastAPI
from mangum import Mangum
from fastapitutorial.public.api import router as api_router

app = FastAPI()


@app.get("/items")
def read_root():
    return {"Hello": "World"}


app.include_router(api_router, prefix="/public")
handler = Mangum(app)
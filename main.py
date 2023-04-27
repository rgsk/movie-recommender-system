from ipynb.fs.full.base import recommend, get_movies
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {
        "message": "Server running on port: 8000"
    }


@app.get("/search")
async def search(movie: str = ""):
    return recommend(movie)


@app.get("/movies")
async def movies():
    return get_movies()

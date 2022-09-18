from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from hello_dask_charts import get_country

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello folks! Let's learn about Spotify Top50 charts"}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}


@app.get("/charts/{title}")
async def read_item(title):
    return {"title": title}


@app.get("/artist/{a}")
async def q_artist(a):
    answer = get_artist({a}) 
    return {"artist": answer}

@app.get("/region/{c_name}")
async def query(result):
    result = get_country(c_name)
    return {"answer".)



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

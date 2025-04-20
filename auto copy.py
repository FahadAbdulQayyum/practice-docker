from typing import Union
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
counter = 0

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/count")
def main():
    global counter
    counter += 1
    return JSONResponse(
        {
            "status": 200,
            "response": f"I've seen {str(counter)} times.\n"
        },
    )

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(
        # "app:app",
        "auto:app",
        # host="0.0.0.0",
        port=2025,
        reload=False
    )
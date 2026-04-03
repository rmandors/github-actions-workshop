from fastapi import FastAPI
from pydantic import BaseModel
from app.calculator import multiply, resta, sum

app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

@app.post("/suma")
def post_suma(body: Numbers) -> dict[str, int]:
    return {"result": sum(body.a, body.b)}

@app.post("/resta")
def post_resta(body: Numbers) -> dict[str, int]:
    return {"result": resta(body.a, body.b)}

@app.post("/multiplicacion")
def post_multiplicacion(body: Numbers) -> dict[str, int]:
    return {"result": multiply(body.a, body.b)}
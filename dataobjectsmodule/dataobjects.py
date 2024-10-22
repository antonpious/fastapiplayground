from pydantic import BaseModel

class Flower(BaseModel):
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float

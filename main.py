import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

import modules.simple_calc


app = FastAPI()


class InputData(BaseModel):
    input_data: str

    class Config:
        schema_extra = {"example": "7+5"}


class OutputData(BaseModel):
    output_data: float

    class Config:
        schema_extra = {"example": "13.234"}


@app.post("/calc", response_model=OutputData)
async def create_hardware_unit(pushed_data: InputData) -> float:
    calculator = modules.simple_calc.SimpleCalculator()
    result = calculator.arithmetic(pushed_data.input_data)
    return OutputData(result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

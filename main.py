import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

import modules.simple_calc
import modules.logger


app = FastAPI()


class CalcRequestDTO(BaseModel):
    input_data: str

    class Config:
        schema_extra = {"example": "7+5"}


class CalcResponseDTO(BaseModel):
    output_data: float

    class Config:
        schema_extra = {"example": "13.234"}


@app.post("/calc", response_model=CalcResponseDTO)
async def create_hardware_unit(pushed_data: CalcRequestDTO):
    calculator = modules.simple_calc.SimpleCalculator()
    result = calculator.calculation_from_string(pushed_data.input_data)

    logger = modules.logger.Logger()
    logger.add_log_to_json(pushed_data.input_data, result)
    return CalcResponseDTO(result)

@app.post("/history", response_model=CalcResponseDTO)
async def create_hardware_unit(pushed_data: CalcRequestDTO):

    #  status: Optional[str] = None

    calculator = modules.simple_calc.SimpleCalculator()
    result = calculator.calculation_from_string(pushed_data.input_data)
    return CalcResponseDTO(result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import UJSONResponse
from pydantic import BaseModel, Field

import modules.storage
import modules.simple_calc

app = FastAPI()


class CalcRequestDTO(BaseModel):
    input_data: str

    class Config:
        schema_extra = {"example": {"input_data": "7+5"}}


class CalcResponseDTO(BaseModel):
    output_data: str

    class Config:
        schema_extra = {"example": {"output_data": "13.234"}}


@app.post("/calc", response_model=CalcResponseDTO)
async def calculation(pushed_data: CalcRequestDTO):
    calculator = modules.simple_calc.SimpleCalculator()
    result = calculator.calculation_from_string(pushed_data.input_data)

    logger = modules.storage.StorageInJson()
    logger.add_log_to_json(pushed_data.input_data, result)

    return {"output_data": result}


class HistoryRequestDTO(BaseModel):
    limit: Optional[int] = None
    status: Optional[str] = None

    class Config:
        schema_extra = {"example": {"limit": 5, "status": "fail"}}


class HistoryResponseDTO(BaseModel):
    output_data: list

    # class Config:
    #     orm_mode = True
    #     schema_extra = {"example": {"output_data": {"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}}}


@app.post("/history", response_model=HistoryResponseDTO)
async def history(pushed_data: HistoryRequestDTO):

    logs = modules.storage.StorageInJson()
    result_logs = logs.read_log_from_json(pushed_data.limit, pushed_data.status)
    return {"output_data": result_logs}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

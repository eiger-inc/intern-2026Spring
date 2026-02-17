"""Pydantic schemas for request / response"""

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str


class ItemResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}

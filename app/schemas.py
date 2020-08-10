from typing import Optional

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    price: int


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None


class ProductFilter(BaseModel):
    name: Optional[str] = None
    price: Optional[str] = None
    limit: int = Field(10, ge=1)
    offset: int = Field(0, ge=0)

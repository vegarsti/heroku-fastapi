from pydantic import BaseModel


class Order(BaseModel):
    id: int
    item: str

    class Config:
        orm_mode = True

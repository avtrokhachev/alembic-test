from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

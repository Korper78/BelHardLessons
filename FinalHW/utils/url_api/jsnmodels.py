from pydantic import BaseModel

class ProdOnPage(BaseModel):
    key: str
    full_name: str

class CurrPage(BaseModel):
    current: int


class OnlinerResponse(BaseModel):
    products: list[ProdOnPage]
    total: int
    page: CurrPage

class GetResponse(BaseModel):
    category: str
    key: str
    depth: int

class PostRequest(BaseModel):
    key: str
    page: int
    id: int

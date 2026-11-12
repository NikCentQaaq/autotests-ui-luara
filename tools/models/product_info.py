from typing import TypedDict, NotRequired


class ProductInfo(TypedDict):
    name: str
    articul: str
    price: int
    size: NotRequired[str]


class ProductCartInfo(TypedDict):
    name: str
    articul: str
    price: int
    size: NotRequired[str]
    quantity: int
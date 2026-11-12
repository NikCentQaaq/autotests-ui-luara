from enum import StrEnum


class Rout(StrEnum):
    MAIN = ""
    CATALOG = "catalog"
    CART = "personal/cart"
    SEARCH = "/search"




class UrlPattern(StrEnum):
    PRICE_ASC = r".*PRICE=asc"
    PRICE_DESC = r".*PRICE=desc"
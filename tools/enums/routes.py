from enum import StrEnum


class Rout(StrEnum):
    MAIN = ""
    CATALOG = "catalog"
    CART = "personal/cart"
    SEARCH = "/search"

    LOGIN = "/login"
    AKTSII = "/aktsii"
    MAGAZINES = "/magazines"




class UrlPattern(StrEnum):
    PRICE_ASC = r".*PRICE=asc"
    PRICE_DESC = r".*PRICE=desc"
from enum import StrEnum


class SortType(StrEnum):
    POPULAR = "popular"
    COMPLETENESS = "komplekt"
    PRICE_ASC = "priceAsc"
    PRICE_DESC = "priceDesc"

    @property
    def url(self):
        return {
            SortType.POPULAR: r".*\?popular=desc",
            SortType.COMPLETENESS: r".*\?sort=komplekt",
            SortType.PRICE_ASC: r".*\?PRICE=asc",
            SortType.PRICE_DESC: r".*\?PRICE=desc",
        }[self]
import re
from enum import StrEnum


class Category(StrEnum):
    RINGS = "Кольца"
    EARRINGS = "Серьги"
    BRACELETS = "Браслеты"
    NECKLACES = "Колье"
    PENDANTS = "Подвески"
    BROOCHES = "Броши"
    CUFFLINKS = "Запонки"


    @property
    @property
    def text_name(self) -> str:
        return {
            Category.RINGS: "Кольцо",
            Category.EARRINGS: "Серьги",
            Category.BRACELETS: "Браслет",
            Category.NECKLACES: "Колье",
            Category.PENDANTS: "Подвес",
            Category.BROOCHES: "Брошь",
            Category.CUFFLINKS: "Запонки",
        }[self]

    @property
    def url_pattern(self):
        return {
            Category.RINGS: re.compile(r".*/catalog/rings/?$"),
            Category.EARRINGS: re.compile(r".*/catalog/earrings/?$"),
            Category.BRACELETS: re.compile(r".*/catalog/bracelets/?$"),
            Category.NECKLACES: re.compile(r".*/catalog/necklace/?$"),
            Category.PENDANTS: re.compile(r".*/catalog/pendants/?$"),
            Category.BROOCHES: re.compile(r".*/catalog/brooches/?$"),
            Category.CUFFLINKS: re.compile(r".*/catalog/studs/?$"),
        }.get(self, self.value)

    @property
    def url_contains(self) -> str:
        return {
            Category.RINGS: "catalog-is-rings",
            Category.EARRINGS: "catalog-is-earrings",
            Category.BRACELETS: "catalog-is-bracelets",
            Category.NECKLACES: "catalog-is-necklaces",
            Category.PENDANTS: "catalog-is-pendants",
            Category.BROOCHES: "catalog-is-brooches",
            Category.CUFFLINKS: "catalog-is-cufflinks",
        }[self]



class Metall(StrEnum):
    GOLD = "Золото"
    SILVER = "Серебро"
    JEWELRY_ALLOY = "Ювелирный сплав"


    @property
    def text_name(self) -> str:
        return {
            Metall.GOLD: "золот",
            Metall.SILVER: "серебр",
            Metall.JEWELRY_ALLOY: ""
        }[self]

    @property
    def url_pattern(self):
        return {
            Metall.GOLD: re.compile(r".*/catalog/gold/?$"),
            Metall.SILVER: re.compile(r".*/catalog/silver/?$"),
            Metall.JEWELRY_ALLOY: re.compile(r".*/catalog/bijouterie/?$"),
        }[self]

    @property
    def url_contains(self) -> str:
        return {
            Metall.GOLD: "metall-is-gold",
            Metall.SILVER: "metall-is-silver",
            Metall.JEWELRY_ALLOY: "metall-is-bijouterie",
        }[self]

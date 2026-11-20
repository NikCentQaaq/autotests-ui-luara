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

    RING = "Кольцо"
    BRACELET = "Браслет"
    PENDANT = "Подвес"  # ПодвесКА/Подвес
    BROOCH = "Брошь"



class Metall(StrEnum):
    GOLD = "Золото"
    SILVER = "Серебро"
    JEWELRY_ALLOY = "Ювелирный сплав"

    @property
    def url_pattern(self):
        return {
            Metall.GOLD: re.compile(r".*/catalog/gold/?$"),
            Metall.SILVER: re.compile(r".*/catalog/silver/?$"),
            Metall.JEWELRY_ALLOY: re.compile(r".*/catalog/bijouterie/?$"),
        }[self]

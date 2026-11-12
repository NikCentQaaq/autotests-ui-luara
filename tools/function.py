


def check_equal(actual, expected):
    assert actual == expected, f"Ожидалось: {expected}, получено: {actual}"

def parse_int_price(value: str) -> int:
    return int(
        value.replace("₽", "")
        .replace("%", "")
        .replace("-", "")
        .replace(" ", "")
        .replace("\xa0", "")
        .strip()
    )

def parse_int_sale(value: str) -> int:
    return int(
        value.replace("%", "")
        .replace("-", "")
        .strip()
    )


def parse_str_articul(value: str) -> str:
    return value.replace("Арт:", "").strip()
import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from elements.button import Button
from elements.image import Image
from elements.link import Link
from elements.text import Text
from tools.enums.category import Category
from tools.function import parse_int_price, parse_int_sale, parse_str_articul


class CardCatalogComponent(BaseComponent):
    def __init__(self, page: Page, container: Locator):
        super().__init__(page)

        self.container = container

        self.name_item = Link(container.locator('a.name'), 'Название украшения')
        self.image = Image(container.locator("div.img img"),"Изображение товара")
        self.articul = Text(container.locator("div.articul"), "Артикул")

        self.price = Text(container.locator('div.price_quantity-new'), 'Цена')
        self.old_price = Text(container.locator('div.price_quantity-old'), 'Старая цена')
        self.sale = Text(container.locator('div.price_quantity-sale'), 'Скидка')

        self.button_add_cart = Button(container.get_by_role('button', name='В корзину'), 'В корзину')





    @allure.step('Проверка, что название товара содержит категорию "{category_name}"')
    def check_name_have_category(self, category_name: Category):

        self.name_item.check_contain_text(category_name.lower())

    @allure.step('Клик по карточке товара')
    def open(self):
        self.name_item.click()

    @allure.step("Получение названия товара")
    def get_name(self) -> str:
        return self.name_item.get_text()

    @allure.step("Получение цены товара")
    def get_price(self) -> int:
        return parse_int_price(self.price.get_text())

    @allure.step("Получение старой цены товара")
    def get_old_price(self)-> int:
        return parse_int_price(self.old_price.get_text())

    @allure.step("Получение размера скидки")
    def get_sale(self) -> int:
        return parse_int_sale(self.sale.get_text())

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self):
        self.button_add_cart.click()

    @allure.step("Проверка элементов карточки товара")
    def check_elements(self):
        self.image.check_visible()
        self.name_item.check_visible()
        self.price.check_visible()

    @allure.step('Проверка, что название товара содержит "{expected}"')
    def check_contains_name(self, expected: str):
        actual_name = self.name_item.get_text()

        assert expected.lower() in actual_name.lower(), f'Ожидалось, что "{actual_name}" содержит "{expected}"'

    @allure.step('Проверка, что артикул содержит "{expected}"')
    def check_contains_articul(self, expected: str):
        actual_articul = parse_str_articul(self.articul.get_text())

        assert expected.lower() in actual_articul.lower() or actual_articul.lower() in expected.lower(), f'Ожидалось: "{expected}", получено: "{actual_articul}"'



    @allure.step("Проверка цены товара")
    def check_price(self, expected: int):
        self.check_equal(self.get_price(), expected)

    @allure.step("Проверка артикула товара")
    def check_articul(self, expected: str):
        self.articul.check_contain_text(expected)








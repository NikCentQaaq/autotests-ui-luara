import allure
from playwright.sync_api import Page, Locator, expect

from components.base_component import BaseComponent
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from elements.link import Link
from elements.text import Text
from tools.function import parse_int_price
from tools.models.product_info import ProductInfo, ProductCartInfo


class CartItemComponent(BaseComponent):

    def __init__(self, page: Page, container: Locator):
        super().__init__(page)

        self.container = container

        self.image = Link(self.container.locator('a.basket-cart_image'), 'Изображение')
        self.name = Link(self.container.locator('div.name a.kc-block_link'), 'Название')
        self.articul = Text(self.container.get_by_text("Артикул:"), 'Артикул')
        self.size = Text(self.container.get_by_text("Размер:"), 'Размер')
        self.material = Text(self.container.get_by_text("Материал:"), 'Материал')
        self.price_quantity = Text(self.container.locator('div.price-new'), 'Цена')

        self.quantity = Input(self.container.get_by_role('textbox', name='Количество'), 'Количество')
        self.button_plus = Button(self.container.get_by_role('button', name='Увеличить количество'), 'Увеличить количество')
        self.button_minus = Button(self.container.get_by_role('button', name='Уменьшить количество'), 'Уменьшить количество')
        self.button_delete = Button(self.container.get_by_role('button', name='Удалить'), 'Удалить')
        self.button_favorite = Button(self.container.get_by_role('button', name='В избранное'), 'В избранное')


    @allure.step('Проверка отображения карточки товара')
    def check_elements(self):
        self.image.check_visible()
        self.name.check_visible()

        self.articul.check_visible()
        self.articul.check_contain_text('Артикул:')

        if self.size.exists(): # если у товара есть элемент размер
            self.size.check_visible()
            self.size.check_contain_text('Размер:')

        self.material.check_visible()
        self.material.check_contain_text('Материал')

        self.price_quantity.check_visible()
        self.quantity.check_visible()

        self.button_plus.check_visible()
        self.button_minus.check_visible()
        self.button_delete.check_visible()
        self.button_favorite.check_visible()



    @allure.step("Получение названия товара")
    def get_name(self) -> str:
        return self.name.get_text()

    @allure.step('Проверка названия товара "{expected}"')
    def check_name(self, expected: str):
        self.check_equal(self.get_name(), expected)




    @allure.step("Получение артикула товара")
    def get_articul(self) -> str:
        articul = self.articul.get_text().replace('Артикул:', '').strip()
        return articul

    @allure.step("Получение размера товара")
    def get_size(self) -> str:
        if not self.size.exists():
            return ""
        size = self.size.get_text().replace("Размер:", "").strip()
        return size


    @allure.step("Получение цены 1 товара")
    def get_price_quantity(self) -> int:
        return parse_int_price(self.price_quantity.get_text())


    @allure.step('Проверка артикула товара "{expected}"')
    def check_articul(self, expected: str):
        self.check_equal(self.get_articul(), expected)

    @allure.step('Проверка размера товара "{expected}"')
    def check_size(self, expected: str):
        self.check_equal(self.get_size(), expected)

    @allure.step('Проверка цены товара {expected} ₽')
    def check_price(self, expected: int):
        self.check_equal(self.get_price_quantity(), expected)

    @allure.step('Получение количества товара')
    def get_quantity(self):
        quantity = self.quantity.get_value()
        return int(quantity)

    @allure.step('Проверка количества товара "{expected}"')
    def check_quantity(self, expected: int):
        self.check_equal(self.get_quantity(), expected)

    @allure.step('Увеличение количества товара на {quantity}')
    def plus_quantity(self, quantity: int = 1):
        for i in range(quantity):
            self.button_plus.click()


    @allure.step('Уменьшение количества товара на {quantity}')
    def minus_quantity(self, quantity: int = 1):
        for i in range(quantity):
            self.button_minus.click()


    @allure.step('Удаление товара из корзины')
    def delete(self):
        self.button_delete.click()





    @allure.step("Получение информации о товаре")
    def get_product_info(self) -> ProductCartInfo:
        return {
            "name": self.get_name(),
            "articul": self.get_articul(),
            "price": self.get_price_quantity(),
            "size": self.get_size(),
            "quantity": self.get_quantity()
        }













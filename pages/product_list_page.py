from random import randint

import allure
from playwright.sync_api import expect

from components.catalog.card_catalog_component import CardCatalogComponent
from components.headers.header_component import HeaderComponent
from pages.base_page import BasePage


class ProductListPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.header = HeaderComponent(page)
        self.cards = page.locator("div.cart-trend")





    @allure.step("Проверка, что список товаров содержит карточки")
    def check_cards_visible(self):
        count = self.cards.count()
        assert count > 0, 'Карточки товаров отсутствуют'

        for i in range(count):
            expect(self.cards.nth(i)).to_be_visible()


    @allure.step("Получение карточки товара с индексом {index}")
    def get_card(self, index: int) -> CardCatalogComponent:
        return CardCatalogComponent(self.page, self.cards.nth(index))



    @allure.step("Получение всех карточек товаров")
    def get_cards(self) -> list[CardCatalogComponent]:
        return [
            self.get_card(i)
            for i in range(self.cards.count())
        ]


    @allure.step('Открытие карточки товара с индексом {index}')
    def open_product_card_by_index(self, index: int):
        self.get_card(index).open()

    @allure.step('Открытие случайной карточки товара')
    def open_product_card_random(self):
        count_cards = self.cards.count()
        index = randint(0, count_cards - 1)

        self.open_product_card_by_index(index)

        return index
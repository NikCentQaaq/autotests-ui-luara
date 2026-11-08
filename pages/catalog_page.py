from random import randint

import allure
from playwright.sync_api import Page, expect

from components.catalog.card_catalog_component import CardCatalogComponent
from components.filter_catalog.catalog_filter_component import CatalogSelectedFilterComponent
from components.headers.catalog_header_component import CatalogHeaderComponent
from components.headers.header_component import HeaderComponent
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.category import Category
from tools.enums.routes import Rout
from tools.enums.sort_type import SortType


class CatalogPage(BasePage):

    ROUTE = Rout.CATALOG

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)
        self.catalog_header = CatalogHeaderComponent(page)

        self.title_category = Text(page.locator('div.h1_b_cat h1'), 'Заголовок Категории')
        self.catalog_selected_filter = CatalogSelectedFilterComponent(page)

        self.cards = page.locator('div.cart-trend')


    @allure.step("Сортировка каталога по значению")
    def sort_products_by_value(self, sort_type: SortType):
        self.catalog_header.select_sort(sort_type)
        self.catalog_header.check_selected_sort(sort_type)





    @allure.step('Проверка элементов Каталога Без фильтрации')
    def check_elements_without_filter(self):
        self.header.check_elements()
        self.catalog_header.check_without_filter()

        self.check_cards_visible()


    @allure.step('Проверка элементов Каталога, отфильтрованного по Категории')
    def check_elements_filter_products(self):
        self.header.check_elements()

        self.catalog_header.check_title_catalog_filter()

        self.title_category.check_visible()

        self.catalog_selected_filter.check_visible()

        self.check_cards_visible()


    @allure.step('Проверка, что каталог содержит карточки товаров')
    def check_cards_visible(self):
        expect(self.cards.first).to_be_visible()

        assert self.cards.count() > 0


    @allure.step('Проверка выбранной категории "{category_name}"')
    def check_selected_filter(self, category_name: Category):
        self.catalog_selected_filter.check_elements(category_name)
        self.title_category.check_have_text(category_name)
        self.catalog_header.check_filter_by_category(category_name)


    @allure.step('Проверка, что все товары относятся к категории "{category_name}"')
    def check_products_category(self, category_name: Category):
        count_cards = self.cards.count()

        for i in range(count_cards):
            card = CardCatalogComponent(self.page,self.cards.nth(i))

            card.check_name_have_category(category_name.lower())


    @allure.step('Открытие карточки товара с индексом {index}')
    def open_product_card_by_index(self, index: int):
        card = CardCatalogComponent(self.page, self.cards.nth(index))
        card.open()

    @allure.step('Открытие случайной карточки товара')
    def open_product_card_random(self):
        count_cards = self.cards.count()
        index = randint(0,count_cards-1)

        card = CardCatalogComponent(self.page, self.cards.nth(index))
        card.open()

        return index

















import re

import allure
from playwright.sync_api import Page

from components.catalog.card_catalog_component import CardCatalogComponent
from components.catalog.filter_catalog.catalog_filter_component import CatalogSelectedFilterComponent
from components.filter.filter_component import FilterComponent
from components.headers.catalog_header_component import CatalogHeaderComponent
from components.headers.header_component import HeaderComponent
from elements.text import Text
from pages.product_list_page import ProductListPage
from tools.enums.category import Category
from tools.enums.routes import Rout
from tools.enums.sort_type import SortType
from tools.function import check_equal


class CatalogPage(ProductListPage):

    ROUTE = Rout.CATALOG

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)
        self.catalog_header = CatalogHeaderComponent(page)
        self.filter = FilterComponent(page)

        self.title_category = Text(page.locator('div.h1_b_cat h1'), 'Заголовок Категории')
        self.catalog_selected_filter = CatalogSelectedFilterComponent(page)


    @allure.step('Проверка загрузки Страницы Каталога')
    def check_loaded_without_filter(self):
        self.check_current_url()
        self.check_elements_without_filter()



    @allure.step("Сортировка каталога по значению")
    def sort_products_by_value(self, sort_type: SortType):
        self.catalog_header.select_sort(sort_type)

        self.catalog_header.check_selected_sort(sort_type)



    @allure.step('Проверка элементов Каталога Без фильтрации')
    def check_elements_without_filter(self):
        self.catalog_header.check_without_filter()
        self.check_cards_visible()


    @allure.step('Проверка элементов Каталога, отфильтрованного по Категории')
    def check_elements_filter_products(self):
        self.catalog_header.check_title_catalog_filter()
        self.title_category.check_visible()

        self.catalog_selected_filter.check_visible()
        self.check_cards_visible()




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



    @allure.step("Получение Списка цен товаров")
    def get_products_prices(self) -> list[int]:
        prices = []

        for i in range(self.cards.count()):
            card = CardCatalogComponent(self.page,self.cards.nth(i))
            prices.append(card.get_price())

        return prices

    @allure.step("Получение Списка названий товаров")
    def get_products_names(self) -> list[str]:
        names = []

        for i in range(self.cards.count()):
            card = CardCatalogComponent(self.page,self.cards.nth(i))
            names.append(card.get_name())

        return names

    @allure.step('Проверка, что названия товаров содержат {value}')
    def check_names_contain_text(self, value: str):
        names = self.get_products_names()

        for name in names:
            assert value.lower() in name.lower(), f'Название товара {name} не содержит {value}'


    @allure.step("Проверка сортировки по возрастанию цены")
    def check_prices_sorted_asc(self):
        prices = self.get_products_prices()

        assert prices == sorted(prices), f'Цены отсортированы неверно'


    @allure.step("Проверка сортировки по убыванию цены")
    def check_prices_sorted_desc(self):
        prices = self.get_products_prices()

        assert prices == sorted(prices, reverse=True), f'Цены отсортированы неверно'


    @allure.step('Проверка, что заголовок каталога содержит {expected}')
    def check_title(self, expected: str):
        self.title_category.check_contain_text(expected)

    @allure.step('Проверка диапазона цен товара')
    def check_range_prices(self, min_price: int, max_price: int):
        prices = self.get_products_prices()

        for price in prices:
            assert min_price <= int(price) <= max_price,  f'Цена товара {price} не входит в диапазон от {min_price} до {max_price}'



    @allure.step('Проверка URL фильтра цены от {min_price} до {max_price}')
    def check_price_filter_url(self, min_price: int, max_price: int):
        pattern = re.compile(rf".*from-{min_price}-to-{max_price}/apply.*")
        self.check_current_url_expected(pattern)

    @allure.step('Проверка количества карточек товаров: {expected_count}')
    def check_cards_count(self, expected_count: int):
        check_equal(self.cards.count(), expected_count)





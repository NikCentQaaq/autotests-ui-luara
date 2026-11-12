import allure
from playwright.sync_api import Page, expect

from components.catalog.card_catalog_component import CardCatalogComponent
from elements.text import Text
from pages.product_list_page import ProductListPage
from tools.enums.routes import Rout


class SearchPage(ProductListPage):

    ROUTE = Rout.SEARCH

    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page.get_by_text('Результаты поиска'), 'Результаты поиска')




    @allure.step('Проверка элементов страницы Поиска')
    def check_elements(self):
        self.header.check_elements()
        self.check_element_text_by_name(self.title)
        self.check_cards_visible()


    @allure.step('Проверка, что результаты поиска содержат "{search_value}"')
    def check_search_results_by_name(self, search_value: str):
        count = self.cards.count()

        for i in range(count):
           item = CardCatalogComponent(self.page, self.cards.nth(i))
           item.check_contains_name(search_value)



    @allure.step('Проверка, что найден товар с артикулом "{articul}"')
    def check_search_results_by_articul(self, articul: str):
        count = self.cards.count()

        for i in range(count):
            item = CardCatalogComponent(self.page, self.cards.nth(i))
            item.check_contains_articul(articul)






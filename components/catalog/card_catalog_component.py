import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from elements.link import Link
from tools.enums.category import Category


class CardCatalogComponent(BaseComponent):
    def __init__(self, page: Page, container: Locator):
        super().__init__(page)

        self.container = container

        # self.container = page.locator('div.cart-trend')

        self.name_item = Link(container.locator('a.name'), 'Название украшения')





    @allure.step('Проверка, что название товара содержит категорию "{category_name}"')
    def check_name_have_category(self, category_name: Category):

        self.name_item.check_contain_text(category_name.lower())


    def open(self):
        self.name_item.click()


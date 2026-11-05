import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.link import Link
from elements.text import Text
from tools.enums.category import Category


class CatalogHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_catalog = Link(page.get_by_text('Каталог украшений'), 'Заголовок "Каталог украшений"')
        self.title_category = Text(page.locator('div.bx-breadcrumb-item span').last, "Заголовок Категории")

    @allure.step('Проверка заголовка "Каталог украшений"')
    def check_title_catalog(self):
        self.check_element(self.title_catalog, 'Каталог украшений')


    @allure.step('Проверка заголовка категории "{category_name}"')
    def check_title_category(self, category_name: Category):
        self.check_element(self.title_category, category_name)

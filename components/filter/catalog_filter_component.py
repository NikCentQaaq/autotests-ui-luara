import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.checkbox import Checkbox
from elements.text import Text
from tools.enums.category import Category


class CatalogFilterComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator('div.gc-filter-param-CATALOG')

        self.title = Text(self.container.get_by_text('Каталог'), 'Каталог')




    def checkbox(self, category: str):
        return Checkbox(self.container.get_by_role("checkbox", name=category), category)

    @allure.step('Выбрать категорию "{category}"')
    def select(self, category: str):
        self.checkbox(category).check()


    @allure.step('Снять категорию "{category}"')
    def unselect(self, category: str):
        self.checkbox(category).uncheck()



    @allure.step('Проверить, что категория "{category}" выбрана')
    def check_selected(self, category: str):
        self.checkbox(category).check_checked()


    @allure.step('Проверить, что категория "{category}" не выбрана')
    def check_not_selected(self, category: str):
        self.checkbox(category).check_not_checked()


    @allure.step('Проверка элементов чекбокса "Каталог"')
    def check_elements(self):
        self.title.check_visible()

        categories = (Category.RINGS, Category.EARRINGS, Category.BRACELETS,
            Category.NECKLACES, Category.PENDANTS, Category.BROOCHES, Category.CUFFLINKS,
        )
        for category in categories:
            self.checkbox(category).check_visible()




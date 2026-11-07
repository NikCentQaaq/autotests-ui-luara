import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.link import Link
from elements.text import Text
from tools.enums.category import Category


class CatalogSelectedFilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator("div.catalog-block_filter")

        self.selected_category = Text(self.container.locator('li.is-selected a'), 'Выбранный фильтр')
        self.reset_button = Link(self.container.locator('li.is-reset a'), 'Сбросить всё')






    @allure.step('Проверка видимости примененных фильтров')
    def check_visible(self):
        self.selected_category.check_visible()
        self.reset_button.check_visible()




    @allure.step('Проверка выбранной категории "{category_name}"')
    def check_selected_category(self, category_name: Category):
        self.check_element(self.selected_category, category_name)

    @allure.step('Проверка Фильтрации категории "{category_name}"')
    def check_elements(self, category_name: Category):
        self.check_selected_category(category_name)
        self.check_element_text_by_name(self.reset_button)








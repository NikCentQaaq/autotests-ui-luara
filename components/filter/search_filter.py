import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text


class SearchFilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.input = Input(page.get_by_placeholder('Найти в фильтрах'), 'Найти в фильтрах')
        self.clear_button = Button(page.get_by_role('button', name='Очистить'), 'Очистить')

        self.empty_search = Text(page.get_by_text('В фильтрах ничего не найдено'), 'В фильтрах ничего не найдено')

    @allure.step('Проверка видимости поиска фильтра')
    def check_elements(self):
        self.input.check_visible()





    @allure.step('Поиск фильтра "{value}"')
    def search(self, value: str):
        self.input.fill(value)


    def click_clear(self):
        self.clear_button.click()


    @allure.step('Проверка, что поиск по фильтрам не дал результатов')
    def check_empty_search(self):
        self.empty_search.check_visible()
        self.empty_search.check_have_text('В фильтрах ничего не найдено')
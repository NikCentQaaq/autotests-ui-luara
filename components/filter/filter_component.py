from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.filter.price_filter_component import PriceFilterComponent
from components.filter.search_filter import SearchFilterComponent
from elements.button import Button
from elements.text import Text


class FilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search = SearchFilterComponent(page)
        self.price = PriceFilterComponent(page)


        self.show_button = Button(page.get_by_role('button', name='Показать'), 'Показать')
        self.reset_button = Button(page.get_by_role('button', name='Сбросить'), 'Сбросить')

        self.result_container = page.locator('div#modef')
        self.result_show = Button(self.result_container.get_by_role('link', name='Показать'), 'Показать Результаты')
        self.result_count = Text(self.result_container.locator('span#modef_num'), 'Счетчик найденных изделий')
        # self.result_title = Text(self.result_container.get_by_text('Найдено: '), 'Найдено')










    def click_show(self):
        self.show_button.click()

    def click_reset(self):
        self.reset_button.click()


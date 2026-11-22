import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.filter.catalog_filter_component import CatalogFilterComponent
from components.filter.metall_filter_component import MetalFilterComponent
from components.filter.price_filter_component import PriceFilterComponent
from components.filter.search_filter import SearchFilterComponent
from elements.button import Button
from elements.text import Text
from tools.enums.category import Metall, Category


class FilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search = SearchFilterComponent(page)
        self.price = PriceFilterComponent(page)
        self.category = CatalogFilterComponent(page)
        self.metall = MetalFilterComponent(page)


        self.show_button = Button(page.get_by_role('button', name='Показать'), 'Показать')
        self.reset_button = Button(page.get_by_role('button', name='Сбросить'), 'Сбросить')

        self.result_container = page.locator('div#modef')
        self.result_show = Button(self.result_container.get_by_role('link', name='Показать'), 'Показать Результаты')
        self.result_count = Text(self.result_container.locator('span#modef_num'), 'Счетчик найденных изделий')
        # self.result_title = Text(self.result_container.get_by_text('Найдено: '), 'Найдено')



    @allure.step('Проверка компонентов фильтра')
    def check_elements(self):
        self.search.check_elements()
        self.price.check_elements()
        self.category.check_elements()
        self.metall.check_elements()

        self.show_button.check_visible()
        self.reset_button.check_visible()


    def click_show(self):
        self.show_button.click()

    def click_reset(self):
        self.reset_button.click()

    def click_show_result(self):
        self.result_show.click()



    @allure.step("Проверка блока найденных результатов")
    def check_block_result(self):
        self.result_show.check_visible()
        self.result_count.check_visible()


    @allure.step("Проверка количества найденных товаров")
    def check_result_count(self):
        self.check_block_result()
        count = int(self.result_count.get_text())
        assert count > 0, "Не найдено ни одного товара"

    @allure.step("Проверка, что найденных товаров 0")
    def check_results_count_zero(self):
        self.check_block_result()
        count = int(self.result_count.get_text())
        assert count == 0, f'Найдено {count} товаров. Ожидалось: 0'




    @allure.step('Установка диапазона цен {min_price} - {max_price}')
    def fill_price_range(self, min_price, max_price):
        self.price.fill_min_price(min_price)
        self.price.fill_max_price(max_price)




    def select_metall(self, metall):
        self.metall.select(metall)

    def select_category(self, category):
        self.category.select(category)

    @allure.step("Проверка, что ни один металл не выбран")
    def check_metall_not_selected(self):
         for metall in Metall:
             self.metall.check_not_selected(metall)

    @allure.step("Проверка, что ни одна категория не выбрана")
    def check_category_not_selected(self):
        for category in Category:
            self.category.check_not_selected(category)









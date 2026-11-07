import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.base_element import BaseElement
from elements.link import Link
from elements.select import Select
from elements.text import Text
from tools.enums.category import Category
from tools.enums.sort_type import SortType


class CatalogHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_catalog = Text(page.get_by_text('Ювелирные украшения'), 'Ювелирные украшения')
        self.block_filter = BaseElement(page.locator('div.gc-filter'), 'Блок Фильтр')
        self.sort = Select(page.locator('select#sortSelect'), 'Сортировка')



        self.title_catalog_filter = Link(page.get_by_text('Каталог украшений'), 'Заголовок "Каталог украшений"')
        self.title_category = Text(page.locator('div.bx-breadcrumb-item span').last, "Заголовок Категории")



    @allure.step("Выбор сортировки по значению")
    def select_sort(self, sort_type: SortType):
        self.sort.select_by_value(value=sort_type)

    @allure.step("Проверка выбранного значения")
    def check_selected_sort(self, sort_type: SortType):
        self.sort.check_selected_value(expected_value=sort_type)











    @allure.step('Проверка заголовков каталога Без фильтраций')
    def check_without_filter(self):
        self.check_element_text_by_name(self.title_catalog)
        self.block_filter.check_visible()
        self.sort.check_visible()




    @allure.step('Проверка заголовка "Каталог украшений"')
    def check_title_catalog_filter(self):
        self.check_element(self.title_catalog_filter, 'Каталог украшений')


    @allure.step('Проверка заголовка категории "{category_name}"')
    def check_title_category(self, category_name: Category):
        self.check_element(self.title_category, category_name)


    @allure.step('Проверка заголовков каталога, фильтрация по Категории')
    def check_filter_by_category(self, category_name: Category):
        self.check_element_text_by_name(self.block_filter)
        self.sort.check_visible()

        self.check_title_catalog_filter()
        self.check_title_category(category_name)


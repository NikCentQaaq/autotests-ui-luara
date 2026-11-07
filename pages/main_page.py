import allure
from playwright.sync_api import Page

from components.concern_catalog.concern_catalog_component import ConcernCatalogComponent
from components.headers.header_component import HeaderComponent
from elements.base_element import BaseElement
from pages.base_page import BasePage
from tools.enums.category import Category
from tools.enums.routes import Rout

class MainPage(BasePage):

    ROUTE = Rout.MAIN

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)

        self.top_slider = BaseElement(page.locator('div.top-slider'), 'Баннер-Слайдер')

        self.catalog_concern = ConcernCatalogComponent(page)

        self.collection_block = BaseElement(page.locator('div.colection-block'), 'Блок коллекции')
        self.trend_block = BaseElement(page.locator('div.trend-block'), 'Блок тренд')
        self.sale_block = BaseElement(page.locator('div.sale-block'), 'Блок акции')
        self.about_block = BaseElement(page.locator('div.about-stage'), 'Блок "О нас"')




    @allure.step('Проверка видимости Верхней навигационной панели (header)')
    def check_header(self):
        self.header.check_elements()

    @allure.step('Проверка видимости блока Каталог')
    def check_catalog_concern(self):
        self.catalog_concern.check_elements()


    @allure.step("Проверка основных блоков")
    def check_blocks(self):
        self.collection_block.check_visible()
        self.trend_block.check_visible()
        self.sale_block.check_visible()
        self.about_block.check_visible()

    @allure.step("Проверка главной страницы")
    def check_elements(self):
        self.check_header()
        self.check_catalog_concern()
        self.check_blocks()



    @allure.step('Открыть категорию "{category_name}"')
    def open_category(self, category_name: Category):
        self.catalog_concern.open_card_by_category(category_name)











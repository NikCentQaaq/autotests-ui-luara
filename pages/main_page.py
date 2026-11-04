import allure
from playwright.sync_api import Page

from components.navigation.header_component import HeaderComponent
from components.navigation.top_header_component import TopHeaderComponent
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)



    @allure.step('Проверка видимости Верхней навигационной панели (header)')
    def check_header(self):
        self.header.check_elements()




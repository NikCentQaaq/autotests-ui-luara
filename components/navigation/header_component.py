import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.middle_header_component import MiddleHeaderComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.top_header_component import TopHeaderComponent
from elements.input import Input
from elements.link import Link




class HeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.top_header = TopHeaderComponent(page)
        self.middle_header = MiddleHeaderComponent(page)


    @allure.step('Проверка компонентов Header')
    def check_elements(self):
        self.top_header.check_elements()
        self.middle_header.check_elements()









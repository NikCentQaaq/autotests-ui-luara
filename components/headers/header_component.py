import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.headers.middle_header_component import MiddleHeaderComponent
from components.headers.top_header_component import TopHeaderComponent
from components.headers.top_panel_component import TopPanelComponent


class HeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.top_header = TopHeaderComponent(page)
        self.middle_header = MiddleHeaderComponent(page)
        self.top_panel = TopPanelComponent(page)


    @allure.step('Проверка компонентов Header')
    def check_elements(self):
        self.top_header.check_elements()
        self.middle_header.check_elements()
        self.top_panel.check_elements()









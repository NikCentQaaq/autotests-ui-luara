from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.navbar_component import NavbarComponent
from elements.header import Header
from elements.input import Input
from elements.link import Link




class HeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = Header(page, 'header-root', 'Шапка сайта')
        self.logo = Link(page, 'header-logo', 'Логотип')
        self.search = Input(page, 'header-search-field', 'Поиск')

        self.navbar = NavbarComponent(page)





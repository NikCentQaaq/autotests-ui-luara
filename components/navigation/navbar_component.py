
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.help_menu_component import HelpMenuComponent
from elements.link import Link


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.wishlist = Link(page, 'header-wishlist-link', 'Избранное')
        self.sign_in = Link(page, 'header-sign-in-trigger', 'Вход')
        self.registration = Link(page, 'header-sign-up-trigger', 'Регистрация')
        self.help = HelpMenuComponent(page)





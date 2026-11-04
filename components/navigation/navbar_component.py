import allure
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

    @allure.step('Проверка видимости Навбара')
    def check_elements(self):
        self.wishlist.check_visible()

        self.sign_in.check_visible()
        self.sign_in.check_have_text('Вход')

        self.registration.check_visible()
        self.registration.check_have_text('Регистрация')

        self.help.check_elements()







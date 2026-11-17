import allure
from playwright.sync_api import Page

from components.headers.header_component import HeaderComponent
from elements.button import Button
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.routes import Rout


class PersonalPage(BasePage):

    ROUTE = Rout.PERSONAL

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)

        self.title = Text(page.get_by_role('heading', name='Личный кабинет'), 'Личный кабинет')
        self.button_logout = Button(page.get_by_role('button', name='Выйти'), 'Выйти')

        self.personal_block = Container(page.locator("section[aria-labelledby='lk_profile_title']"), 'Блок "Личные данные"')
        self.security_block = Container(page.locator("section#security"), 'Блок "Вход и Безопасность"')
        self.bonus_block = Container(page.locator("section[aria-labelledby='lk_bonus_title']"), 'Блок "Бонусы"')
        self.order_block = Container(page.locator("section[aria-labelledby='lk_order_title']"), 'Блок "Заказы"')

    @allure.step('Проверка элементов Личного кабинета')
    def check_elements(self):
        self.check_element_text_by_name(self.title)
        self.check_element_text_by_name(self.button_logout)

        self.personal_block.check_visible()
        self.security_block.check_visible()
        self.bonus_block.check_visible()
        self.order_block.check_visible()

    @allure.step('Нажатие кнопка "Выход"')
    def logout(self):
        self.button_logout.click()

import allure
from playwright.sync_api import Page

from components.headers.header_component import HeaderComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.routes import Rout


class LoginPage(BasePage):

    ROUTE = Rout.LOGIN

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)

        self.title = Text(page.get_by_role("heading", name="Вход"), 'Вход')
        self.description = Text(page.get_by_text('Введите логин и пароль — откроются заказы и бонусы.'), 'Введите логин и пароль — откроются заказы и бонусы.')

        self.input_login = Input(page.get_by_role('textbox', name='Логин'), 'Логин')
        self.input_password = Input(page.get_by_role('textbox', name='Пароль'), 'Пароль')
        self.login_button = Button(page.get_by_role('button', name='Войти'), 'Войти')

        self.alert = Text(page.get_by_role("alert"),"Неверный логин или пароль.")

    @allure.step("Проверка элементов страницы Авторизации")
    def check_elements(self):
        self.header.check_elements()

        self.check_element_text_by_name(self.title)
        self.check_element_text_by_name(self.description)
        self.check_element_text_by_name(self.input_login)
        self.check_element_text_by_name(self.input_password)
        self.check_element_text_by_name(self.login_button)

    @allure.step("Ввод логина: {value}")
    def login_input(self, value: str):
        self.input_login.fill(value)

    @allure.step("Ввод пароля")
    def password_input(self, value: str):
        self.input_password.fill(value)

    @allure.step("Нажатие кнопки «Войти»")
    def click_login_button(self):
        self.login_button.click()

    @allure.step("Авторизация пользователя")
    def fill_login_form(self, login: str, password: str):
        self.login_input(login)
        self.password_input(password)
        self.login_button.click()

    @allure.step("Проверка сообщения об ошибке авторизации")
    def check_alert_wrong_data(self):
        self.check_element_text_by_name(self.alert)



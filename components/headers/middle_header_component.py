import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.container import Container
from elements.input import Input
from elements.link import Link
from elements.text import Text


class MiddleHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = Container(page.locator('div.header-mid'), 'Middle Header')

        self.logo = Link(page.locator('div.header-mid').get_by_role('link', name='Luara'), 'Логотип Luara')
        self.catalog_button = Button(page.get_by_role('button', name='Каталог'), 'Каталог')

        self.search_input = Input(page.get_by_placeholder('Искать на Luara'), 'Поиск')
        self.search_button = Button(page.get_by_role('button', name='Найти'), 'Найти')

        self.login = Link(page.get_by_role('link', name='Войти'), name='Войти')
        self.personal = Link(page.get_by_role('link', name='Профиль'), 'Профиль')

        self.orders = Link(page.get_by_role('link', name='Заказы'), name='Заказы')
        self.favorites = Link(page.get_by_role('link', name='Избранное'), name='Избранное')
        self.cart = Link(page.get_by_role('link', name='Корзина'), name='Корзина')

        self.num_cart = Text(page.locator('span.headCartNum'), 'Кол-во в Корзине')




    @allure.step("Проверка элементов Middle Header")
    def check_elements(self, authorized: bool = False):
        self.logo.check_visible()
        self.search_input.check_visible()

        self.check_element_text_by_name(self.catalog_button)
        self.check_element_text_by_name(self.search_button)

        if authorized:
            self.check_element_text_by_name(self.personal)
        else:
            self.check_element_text_by_name(self.login)

        self.check_element_text_by_name(self.orders)
        self.check_element_text_by_name(self.favorites)

        self.cart.check_visible()
        self.cart.check_contain_text("Корзина")


    @allure.step('Нажатие на корзину')
    def click_cart(self):
        self.cart.click()

    @allure.step('Ввод "{value}" в поле Поиска')
    def input_search(self, value: str):
        self.search_input.fill(value)


    @allure.step('Нажатие кнопки "Поиск')
    def click_search_button(self):
        self.search_button.click()

    @allure.step('Нажатие на Логотип')
    def click_logo(self):
        self.logo.click()

    @allure.step('Нажатие на "Войти"')
    def click_login(self):
        self.login.click()















import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.link import Link


class MiddleHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator(".header-mid")

        self.logo = Link(self.container.get_by_role('link', name='Luara'), 'Логотип Luara')
        self.catalog_button = Button(self.container.get_by_role('button', name='Каталог'), 'Каталог')
        self.search_input = Input(self.container.get_by_placeholder('Искать на Luara'), 'Поиск')
        self.search_button = Button(self.container.get_by_role('button', name='Найти'), 'Найти')

        self.login = Link(self.container.get_by_role('link', name='Войти'), name='Войти')
        self.orders = Link(self.container.get_by_role('link', name='Заказы'), name='Заказы')
        self.favorites = Link(self.container.get_by_role('link', name='Избранное'), name='Избранное')
        self.cart = Link(self.container.get_by_role('link', name='Корзина'), name='Корзина')


    @allure.step('Проверка элементов Middle Header')
    def check_elements(self):
        self.logo.check_visible()
        self.search_input.check_visible()

        self.check_element(self.catalog_button)
        self.check_element(self.search_button)
        self.check_element(self.login)
        self.check_element(self.orders)
        self.check_element(self.favorites)
        self.check_element(self.cart)












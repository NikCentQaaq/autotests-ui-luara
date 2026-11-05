import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.button import Button
from elements.text import Text


class NavConcernComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.container = page.locator('div.concern-nav')

        self.back_button = Button(self.container.get_by_role('button', name='Назад'), 'Назад')
        self.next_button = Button(self.container.get_by_role('button', name='Вперёд'), 'Вперёд')
        self.count_nav = Text(self.container.locator('p.concern-nav_count'), 'Счетчик')


    @allure.step('Проверка элементов Навигации каталога')
    def check_elements(self):
        self.back_button.check_visible()
        self.next_button.check_visible()
        self.count_nav.check_visible()







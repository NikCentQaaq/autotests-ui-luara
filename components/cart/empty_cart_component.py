import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text


class EmptyCartComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator("div.basket-empty")

        self.icon = Image(self.container.locator('div.basket-empty_icon'), 'Иконка')
        self.title = Text(self.container.get_by_text('Ваша корзина пуста'), 'Заголовок')
        self.description = Text(self.container.get_by_text('Выберите украшение в каталоге'), 'Описание')

        self.catalog_button = Button(self.container.get_by_role('link', name='Перейти в каталог'), 'Перейти в каталог')


    @allure.step('Проверка элементов пустой корзины')
    def check_elements(self):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text('Ваша корзина пуста')
        self.description.check_visible()
        self.description.check_have_text('Выберите украшение в каталоге')


import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text


class CardConcernComponent(BaseComponent):
    def __init__(self, page: Page, container: Locator):
        super().__init__(page)
        self.container = container

        self.card = Button(container.locator("a.concern-card"), "Карточка категории")

        self.image = Image(container.locator("span.concern-card_media img"), 'Изображение')
        self.name = Text(container.locator('span.concern-card_name'), 'Название')
        self.count = Text(container.locator('span.concern-card_count'), 'Кол-во товаров')

        self.go_button = Button(container.locator('span.concern-card_go'), 'Переход к товарам')


    @allure.step('Проверка элементов Карточки')
    def check_elements(self):
        self.image.check_visible()
        self.name.check_visible()
        self.count.check_visible()
        self.go_button.check_visible()


    @allure.step('Открытие категории')
    def click(self):
        self.card.click()







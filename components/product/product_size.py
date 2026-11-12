import re
from random import randrange

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
import allure


class SizeProductComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator("div.sizing-box")

        self.size = self.container.locator("div.sizing-check")
        self.active_size = self.container.locator(".sizing-check.active")


    @allure.step('Проверка видимости Размеров')
    def is_visible(self) -> bool:
        return self.container.is_visible(timeout=1000)



    @allure.step("Получение выбранного размера")
    def get_selected_size(self) -> str:

        if self.active_size.count() == 0:
            return ""
        expect(self.active_size).to_be_visible()
        return self.active_size.inner_text().strip()



    @allure.step('Выбор рандомного размера из доступных')
    def select_random_size(self):
        count = self.size.count()
        index = randrange(count)
        size = self.size.nth(index)
        selected_size = size.text_content().strip()

        with allure.step(f'Выбран размер {selected_size}'):
            size.click()
            expect(size).to_have_class(re.compile(r"\bactive\b"))


    @allure.step("Выбор размера при необходимости")
    def select_size_if_needed(self):

        if self.size.count() == 0:  # Размеров нет
            return

        if self.active_size.count() > 0:   # Размер 1 и он уже выбран
            with allure.step(f'Размер уже выбран "{self.get_selected_size()}"'):
                return

        # Размеры есть, но ни один не выбран
        self.select_random_size()
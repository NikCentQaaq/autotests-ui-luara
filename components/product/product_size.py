import re
from random import randrange

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
import allure

from elements.text import Text


class SizeProductComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator("div.sizing-box")

        self.size = self.container.locator("div.sizing-check")
        self.active_size = self.container.locator(".sizing-check.active")

        self.split = Text(page.get_by_test_id('split-payment-amount'), 'Яндекс Сплит')


    @allure.step("Получение выбранного размера")
    def get_selected_size(self) -> str:

        if self.active_size.count() == 0:
            return ""
        expect(self.active_size).to_be_visible()
        return self.active_size.inner_text().strip()



    @allure.step('Выбор рандомного размера из доступных')
    def select_random_size(self):
        # Загрузка элемента ЯндексСплит, который сбивает выбор размера

        if self.split.get_locator().is_visible(timeout=1000):
            self.split.check_visible()

        expect(self.size.first).to_be_visible()

        count = self.size.count()
        size = self.size.nth(randrange(count))

        selected_size = size.inner_text().strip()

        with allure.step(f'Выбран размер "{selected_size}"'):

            expect(size).to_be_visible()
            expect(size).to_be_enabled()

            size.click()

            expect(size).to_have_class(re.compile(r"\bactive\b"))
            expect(self.active_size).to_have_count(1)
            expect(self.active_size).to_have_text(selected_size)



    @allure.step("Выбор размера при необходимости")
    def select_size_if_needed(self):
        count = self.size.count()

        if count == 0:
            return

        if self.active_size.count() == 1:
            with allure.step(f'Размер "{self.get_selected_size()}" уже выбран'):
                return

        if count == 1:
            size = self.size.first

            expect(size).to_be_visible()
            expect(size).to_be_enabled()

            selected_size = size.inner_text().strip()

            with allure.step(f'Выбран единственный размер "{selected_size}"'):
                size.click()

                expect(size).to_have_class(
                    re.compile(r"\bactive\b")
                )
                expect(self.active_size).to_have_count(1)
                expect(self.active_size).to_have_text(selected_size)

            return

        self.select_random_size()

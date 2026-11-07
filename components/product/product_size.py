from random import randrange

from playwright.sync_api import Page

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



    @allure.step('Выбор рандомного размера из доступных')
    def select_random_size(self):
        count = self.size.count()
        index = randrange(count)
        size = self.size.nth(index)
        selected_size = size.text_content().strip()

        with allure.step(f'Выбран размер {selected_size}'):
            size.click()

        return selected_size

    @allure.step("Выбор размера при необходимости")
    def select_size_if_needed(self) -> str:

        if self.size.count() == 0:  # Размеров нет
            return ""

        if self.active_size.count() > 0:   # Размер 1 и он уже выбран
            selected_size = self.active_size.inner_text().strip()

            with allure.step(f'Размер уже выбран "{selected_size}"'):
                return selected_size

        # Размеры есть, но ни один не выбран
        return self.select_random_size()
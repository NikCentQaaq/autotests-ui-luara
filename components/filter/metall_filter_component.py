import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.checkbox import Checkbox
from elements.text import Text
from tools.enums.category import Metall


class MetalFilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.container = page.locator("div.gc-filter-param-METALL")

        self.title = Text(self.container.locator(".bx-filter-parameters-box-title"),"Металл")



    def checkbox(self, metall: str):
        return Checkbox(self.container.get_by_role("checkbox", name=metall), metall)



    @allure.step('Проверка элементов чекбокса "Металл"')
    def check_elements(self):
        self.title.check_visible()

        metalls = [Metall.GOLD, Metall.SILVER, Metall.JEWELRY_ALLOY]
        for metall in metalls:
            self.checkbox(metall).check_visible()




    @allure.step('Выбрать металл "{metal}"')
    def select(self, metal: str):
        self.checkbox(metal).check()

    @allure.step('Снять выбор металла "{metal}"')
    def unselect(self, metal: str):
        self.checkbox(metal).uncheck()

    @allure.step('Проверить, что металл "{metal}" выбран')
    def check_selected(self, metal: str):
        self.checkbox(metal).check_checked()

    @allure.step('Проверить, что металл "{metal}" не выбран')
    def check_not_selected(self, metal: str):
        self.checkbox(metal).check_not_checked()



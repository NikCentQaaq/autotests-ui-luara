import allure
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.headers.middle_header_component import MiddleHeaderComponent
from components.headers.top_header_component import TopHeaderComponent
from components.headers.top_panel_component import TopPanelComponent
from tools.function import check_equal


class HeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.top_header = TopHeaderComponent(page)
        self.middle_header = MiddleHeaderComponent(page)
        self.top_panel = TopPanelComponent(page)


    @allure.step('Проверка компонентов Header')
    def check_elements(self):
        self.top_header.check_elements()
        self.middle_header.check_elements()
        self.top_panel.check_elements()

    @allure.step("Открытие корзины")
    def open_cart(self):
        self.middle_header.click_cart()



    @allure.step('Получение количества товаров в корзине')
    def get_num_cart(self) -> int:

        return int(self.middle_header.num_cart.get_text())


    @allure.step('Проверка количества товаров в корзине')
    def check_quantity(self, expected: int):
        expect(self.middle_header.num_cart.get_locator()
        ).to_have_text(str(expected))

    @allure.step('Поиск товара "{value}"')
    def search(self, value: str):
        self.middle_header.input_search(value)
        self.middle_header.click_search_button()








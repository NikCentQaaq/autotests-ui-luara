import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.link import Link
from elements.text import Text


class CartSummaryComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator("div.basket-summary")

        self.title = Text(self.container.locator("div.total span").first,"Итого")
        self.total_price = Text(self.container.locator("div.total span").last,"Итого")
        self.total_quantity = Text(self.container.locator("div.goods i"), 'Кол-во товаров')
        self.discount = Text(self.container.locator("div.discount").first.locator("span").last, 'Сумма скидок')

        self.promocode_input = Input(self.container.get_by_placeholder('Введите промокод'), 'Введите промокод')
        self.button_promocode = Button(self.container.get_by_role('button', name='Применить'), 'Применить')

        self.checkout_button = Link(self.container.get_by_role('link', name='Перейти к оформлению'), 'Перейти к оформлению')
        self.continue_shopping_button = Link(self.container.get_by_role("link", name="Продолжить покупки"),"Продолжить покупки")





    @allure.step("Проверка отображения блока итогов корзины")
    def check_elements(self):
        self.check_element_text_by_name(self.title)
        self.total_price.check_visible()
        self.total_quantity.check_visible()
        self.discount.check_visible()

        self.promocode_input.check_visible()
        self.check_element_text_by_name(self.button_promocode)

        self.check_element_text_by_name(self.checkout_button)
        self.check_element_text_by_name(self.continue_shopping_button)


    @allure.step("Получение итоговой стоимости")
    def get_total_price(self) -> int:
        price = self.total_price.get_text().replace("₽", "").replace(" ", "").replace("\xa0", "")
        return int(price)


    @allure.step('Проверка итоговой стоимости "{expected}" ₽')
    def check_total_price(self, expected: int):
        self.check_equal(self.get_total_price(), expected)


    @allure.step("Получение количества товаров")
    def get_total_quantity(self) -> int:
        return int(self.total_quantity.get_text())


    @allure.step('Проверка количества товаров "{expected}"')
    def check_total_quantity(self, expected: int):
        self.check_equal(self.get_total_quantity(), expected)



    @allure.step("Получение суммы скидки")
    def get_discount(self) -> int:
        discount = (
            self.discount.get_text().replace("₽", "").replace("−", "") .replace("-", "")
            .replace(" ", "").replace("\xa0", ""))

        return int(discount)

    @allure.step('Проверка суммы скидки "{expected}" ₽')
    def check_discount(self, expected: int):
        self.check_equal(self.get_discount(), expected)




    @allure.step('Ввод промокода "{promocode}"')
    def fill_promocode(self, promocode: str):
        self.promocode_input.fill(promocode)

    @allure.step("Применение промокода")
    def apply_promocode(self):
        self.button_promocode.click()




















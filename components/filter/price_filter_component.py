import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.slider import Slider
from elements.text import Text


class PriceFilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator('div.prices')


        self.title = Text(page.get_by_text('Цена '), 'Цена')

        self.min_input = Input(page.locator('input.min-price'), 'Минимальная цена')
        self.max_input = Input(page.locator('input.max-price'), 'Максимальная цена')

        self.left_slider = Slider(self.container.get_by_role('button', name='Цена от'),'Ползунок "Цена от"')
        self.right_slider = Slider(self.container.get_by_role('button', name='Цена до'),'Ползунок "Цена до"')



    @allure.step("Проверка фильтра цены")
    def check_elements(self):
        self.title.check_visible()
        self.min_input.check_visible()
        self.max_input.check_visible()
        self.left_slider.check_visible()
        self.right_slider.check_visible()


    @allure.step('Ввод Максимальной цены {value}')
    def fill_max_price(self, value):
        self.max_input.fill(value)
        self.max_input.press('Enter')

        self.check_max_price(value)

    @allure.step('Ввод Минимальной цены {value}')
    def fill_min_price(self, value):
        self.min_input.fill(value)
        self.min_input.press('Enter')

        self.check_min_price(value)




    @allure.step('Переместить правый ползунок на {offset}px')
    def move_right_slider(self, offset: int):
        self.right_slider.move(offset)

    @allure.step('Переместить левый ползунок на {offset}px')
    def move_left_slider(self, offset: int):
        self.left_slider.move(offset)



    @allure.step('Проверка минимальной цены "{value}"')
    def check_min_price(self, value: int):
        self.min_input.check_have_value(str(value))

    @allure.step('Проверка максимальной цены "{value}"')
    def check_max_price(self, value: int):
        self.max_input.check_have_value(str(value))

















import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.slider import Slider


class PriceFilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator('div.gc-filter-parameters-box.prices')


        self.title = Button(page.get_by_text('Цена '), 'Цена')

        self.min_input = Input(page.locator('input.min-price'), 'Минимальная цена')
        self.max_input = Input(page.locator('input.max-price'), 'Максимальная цена')

        self.left_slider = Slider(self.container.get_by_role('button', name='Цена от'),'Ползунок "Цена от"')
        self.right_slider = Slider(self.container.get_by_role('button', name='Цена до'),'Ползунок "Цена до"')



    @allure.step('Ввод Максимальной цены {value}')
    def fill_max_price(self, value):
        self.max_input.fill(value)
        self.max_input.press('Enter')

    @allure.step('Ввод Минимальной цены {value}')
    def fill_min_price(self, value):
        self.min_input.fill(value)
        self.min_input.press('Enter')

    @allure.step('Установка диапазона цен {min_price} - {max_price}')
    def fill_price_range(self, min_price, max_price):
        self.fill_min_price(min_price)
        self.fill_max_price(max_price)





    @allure.step('Переместить правый ползунок на {offset}px')
    def move_right_slider(self, offset: int):
        self.right_slider.move(offset)

    @allure.step('Переместить левый ползунок на {offset}px')
    def move_left_slider(self, offset: int):
        self.left_slider.move(offset)

















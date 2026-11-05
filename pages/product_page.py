import allure
from playwright.sync_api import Page

from components.headers.catalog_header_component import CatalogHeaderComponent
from elements.image import Image
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.category import Category


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.catalog_header = CatalogHeaderComponent(page)

        self.image = Image(page.locator('img.img_body'), 'Изображение')
        self.name_product = Text(page.locator('div.bx h1.ttl'), 'Название')
        self.price = Text(page.locator('div.price div.kc-current_price'), 'Цена')
        self.add_button = Link(page.get_by_role('link', name='Добавить в корзину'), 'Добавить в корзину')


    @allure.step('Проверка заголовка каталога для категории "{category_name}"')
    def check_catalog_header(self, category_name: Category):
        self.catalog_header.check_title_category(category_name)
        self.catalog_header.check_title_catalog()


    @allure.step('Проверка, что название товара содержит категорию "{category_name}"')
    def check_name_have_category(self, category_name: Category):
        self.name_product.check_contain_text(category_name.lower())


    @allure.step('Проверка элементов на странице продукта')
    def check_elements(self):
        self.image.check_visible()
        self.name_product.check_visible()
        self.price.check_visible()

        self.add_button.check_visible()
        self.add_button.check_contain_text('Добавить в корзину')





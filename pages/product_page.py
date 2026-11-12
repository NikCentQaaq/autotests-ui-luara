import allure
from playwright.sync_api import Page, expect

from components.headers.catalog_header_component import CatalogHeaderComponent
from components.headers.header_component import HeaderComponent
from components.product.product_size import SizeProductComponent
from elements.image import Image
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.category import Category
from tools.function import parse_int_price
from tools.models.product_info import ProductInfo


class ProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)
        self.catalog_header = CatalogHeaderComponent(page)
        self.size = SizeProductComponent(page)

        self.image = Image(page.locator('img.img_body'), 'Изображение')
        self.name_product = Text(page.locator('div.bx h1.ttl'), 'Название')
        self.price = Text(page.locator('div.kc-current_price'), 'Цена')
        self.add_button = Link(page.get_by_role('link', name='Добавить в корзину'), 'Добавить в корзину')

        self.popup_success_add_product = Text(page.locator('div.notyf__message'), 'Товар успешно добавлен в корзину')

        self.articul = Text(page.get_by_text('Арт:'), 'Артикул')

    @allure.step("Проверка уведомления об успешном добавлении товара")
    def check_popup_success_add(self):
        locator = self.popup_success_add_product.get_locator()

        expect(locator).to_be_visible()



    @allure.step('Получение Артикула товара')
    def get_product_articul(self):
        return self.articul.get_text().replace("Арт:", "").strip()

    @allure.step('Получение Названия и Артикула товара')
    def get_product_name_and_articul(self) -> str:
        name = self.name_product.get_text()
        return name

    @allure.step('Получение Названия товара')
    def get_product_name(self):
        name = self.get_product_name_and_articul().replace(f"{self.get_product_articul()}", "").strip()
        return name



    @allure.step('Получение Цены товара')
    def get_product_price(self) -> int:
        return parse_int_price(self.price.get_text())


    @allure.step('Получение данных продукта')
    def get_product_info(self) -> ProductInfo:
        return {
            "name": self.get_product_name(),
            "articul": self.get_product_articul(),
            "price_quantity": self.get_product_price(),
            "size": self.size.get_selected_size()
        }

    @allure.step("Добавление товара в корзину")
    def add_product_to_cart(self):
        self.add_button.click()




    def check_num_cart_into_header(self, expected_num: int):
        self.header.check_quantity(expected_num)






    @allure.step('Проверка заголовка каталога для категории "{category_name}"')
    def check_catalog_header(self, category_name: Category):
        self.catalog_header.check_title_category(category_name)
        self.catalog_header.check_title_catalog_filter()


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





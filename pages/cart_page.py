import allure
from playwright.sync_api import Page, expect

from components.cart.cart_item_component import CartItemComponent
from components.cart.cart_summary_component import CartSummaryComponent
from components.cart.empty_cart_component import EmptyCartComponent
from components.headers.header_component import HeaderComponent
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.routes import Rout
from tools.function import check_equal
from tools.models.product_info import ProductInfo


class CartPage(BasePage):
    ROUTE = Rout.CART

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)
        self.summary = CartSummaryComponent(page)
        self.empty_cart = EmptyCartComponent(page)

        self.items = page.locator("div.basket-block_item:not(.is-gift)")  # CartItemComponent


        self.title = Text(page.get_by_text('Корзина'), "Корзина")
        self.gift = Container(page.locator("div.basket-block_item.is-gift"), 'Блок Подарок')




    @allure.step("Проверка элементов страницы корзины")
    def check_elements(self):
        self.summary.check_elements()
        self.title.check_visible()
        self.title.check_contain_text('Корзина')

        self.check_items_visible()
        self.gift.check_visible()



    @allure.step("Получение товара №{index}")
    def get_item(self, index: int) -> CartItemComponent:
        item = CartItemComponent(self.page, self.items.nth(index))
        return item

    @allure.step("Получение количества товара №{index}")
    def get_item_quantity(self, index: int) -> int:
        item = self.get_item(index)
        count = item.get_quantity()
        return int(count)


    @allure.step("Проверка отображения товаров")
    def check_items_visible(self):
        expect(self.items.first).to_be_visible(timeout=10000)

        for i in range(self.items.count()):
            self.get_item(i).check_elements()

    @allure.step("Проверка названия товара №{index}")
    def check_name_item(self, index: int, expected_name: str):
        self.get_item(index).check_name(expected_name)

    @allure.step("Проверка размера товара №{index}")
    def check_size_item(self, index: int, expected_size: int):
        self.get_item(index).check_size(expected_size)

    @allure.step("Проверка артикула товара №{index}")
    def check_articul_item(self, index: int, expected_articul: str):
        self.get_item(index).check_articul(expected_articul)


    @allure.step("Удаление товара №{index}")
    def delete_item(self, index: int):
        self.get_item(index).delete()



    @allure.step("Увеличение количества товара №{index} на {quantity}")
    def plus_quantity_item(self, index: int, quantity: int = 1):
        old_price = self.summary.total_price.get_text().strip()

        self.get_item(index).plus_quantity(quantity)

        expect(self.summary.total_price.locator).not_to_have_text(str(old_price))

    @allure.step("Уменьшение количества товара №{index} на {quantity}")
    def minus_quantity_item(self, index: int, quantity: int = 1):
        old_price = self.summary.total_price.get_text()

        self.get_item(index).minus_quantity(quantity)

        expect(self.summary.total_price.locator).not_to_have_text(str(old_price))



    @allure.step('Проверка количества товара №{index}')
    def check_item_quantity(self, index: int, expected_quantity: int):

        self.get_item(index).check_quantity(expected_quantity)




    @allure.step('Проверка общей стоимости "{expected_price}" ₽')
    def check_total_price(self, expected_price: int):
        self.summary.check_total_price(expected_price)

    @allure.step('Проверка общего количества товаров "{expected}"')
    def check_total_quantity_expected(self, expected: int):
        self.summary.check_total_quantity(expected)

    @allure.step('Проверка общей скидки "{expected}" ₽')
    def check_discount(self, expected: int):
        self.summary.check_discount(expected)

    @allure.step('Применение промокода "{promocode}"')
    def apply_promocode(self, promocode: str):
        self.summary.fill_promocode(promocode)
        self.summary.apply_promocode()

    @allure.step("Переход к оформлению заказа")
    def open_checkout(self):
        self.summary.checkout_button.click()

    @allure.step("Продолжить покупки")
    def continue_shopping(self):
        self.summary.continue_shopping_button.click()

    @allure.step("Расчет общего количества товаров по каждому товару")
    def get_items_count(self) -> int:
        count = 0

        for i in range(self.items.count()):
            count += self.get_item(i).get_quantity()

        return count

    @allure.step("Проверка общего количества товаров в корзине")
    def check_total_quantity(self):
        check_equal(self.summary.get_total_quantity(), self.get_items_count())




    @allure.step("Проверка пустой корзины")
    def check_cart_is_empty(self):

        self.title.check_visible()
        self.title.check_contain_text('Корзина')

        self.empty_cart.check_elements()




    @allure.step("Ожидание загрузки товаров в корзине")
    def wait_items_loaded(self):
        expect(self.items.first).to_be_visible(timeout=10000)

    @allure.step("Получение данных товара в корзине №{index}")
    def get_product_info(self, index: int):
        product = self.get_item(index)
        return product.get_product_info()



    @allure.step("Проверка добавленного товара в корзине")
    def check_added_product(self,product: dict, quantity: int = 1,   index: int = 0):

        self.check_name_item(index, product["name"])

        if product["size"]:
            self.check_size_item(index, product["size"])

        self.check_articul_item(index, product["articul"])
        self.check_item_quantity(index, quantity)
        self.check_total_price(product["price"])
        self.check_total_quantity()

    @allure.step('Проверка количества карточек товаров: {expected}')
    def check_count_items(self, expected: int):
        actual = self.items.count()
        check_equal(actual, expected)


    @allure.step('Проверка товара в корзине по Артикулу')
    def check_added_product_by_articul(self, product: ProductInfo):
        item = self.get_item_by_articul(product["articul"])

        item.check_name(product["name"])
        item.check_articul(product["articul"])
        item.check_price(product["price"])

        if product["size"]:
            item.check_size(product["size"])

    @allure.step('Проверка товаров в корзине')
    def check_products(self, expected_products: list[ProductInfo]):
        self.check_count_items(len(expected_products))

        for product in expected_products:
            self.check_added_product_by_articul(product)

    @allure.step('Получение товара по артикулу')
    def get_item_by_articul(self, articul: str) -> CartItemComponent:
        locator = self.items.filter(has_text=articul)

        expect(locator).to_have_count(1)

        return CartItemComponent(self.page, locator.first)


    @allure.step('Удаление товара "{articul}"')
    def delete_item_by_articul(self, articul: str):

        self.get_item_by_articul(articul).delete()

    @allure.step('Увеличение кол-ва товара "{articul}"')
    def plus_quantity_by_articul(self, articul: str, quantity: int = 1):
        old_price = self.summary.total_price.get_text()

        self.get_item_by_articul(articul).plus_quantity(quantity)

        expect(self.summary.total_price.locator).not_to_have_text(old_price)


    @allure.step('Уменьшение кол-ва товара "{articul}"')
    def minus_quantity_by_articul(self, articul: str, quantity: int = 1):
        old_price = self.summary.total_price.get_text()

        self.get_item_by_articul(articul).minus_quantity(quantity)

        expect(self.summary.total_price.locator).not_to_have_text(old_price)



    @allure.step('Проверка кол-ва товара {quantity} по артикулу {articul}')
    def check_quantity_by_articul(self, articul: str, quantity: int):
        item = self.get_item_by_articul(articul)
        item.check_quantity(quantity)




    @allure.step('Проверка общей стоимости нескольких товаров')
    def check_total_price_products(self, products: list[ProductInfo]):
        expected = self.get_sum_price_products(products)
        self.check_total_price(expected)


    @allure.step('Получение суммы стоимости всех товаров')
    def get_sum_price_products(self, products: list[ProductInfo]):
        price = sum(product["price"] for product in products)
        return price

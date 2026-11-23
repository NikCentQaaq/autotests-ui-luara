import allure
import pytest

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from tools.enums.allure_enum import AllureEpic, AllureFeature, AllureStory

@allure.epic(AllureEpic.UI)
@allure.feature(AllureFeature.CART)
class TestCart:



    @allure.story(AllureStory.ADD_TO_CART)
    @allure.title('Добавление товара в корзину из карточки товара')
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "opened_product", # параметр передается в фикстуру!
        [
            pytest.param(0, id="product_1"),
            pytest.param(10, id="product_11")
        ],
        indirect=True
    )
    def test_add_1_product_to_cart(self, opened_product: ProductPage, cart_page: CartPage):

        product = opened_product.add_product_to_cart()

        opened_product.check_num_cart_into_header(1)

        opened_product.header.open_cart_page()
        cart_page.check_loaded()

        cart_page.check_added_product(product)

    @allure.story(AllureStory.ADD_TO_CART)
    @allure.title("Добавление двух товаров в корзину")
    @pytest.mark.smoke
    def test_add_2_product_to_cart(self, opened_catalog_page: CatalogPage, product_page: ProductPage, cart_page: CartPage):

        opened_catalog_page.open_product_card_by_index(index=5)
        product_page.check_loaded()

        product1 = product_page.add_product_to_cart()

        product_page.go_back()
        opened_catalog_page.check_loaded()

        opened_catalog_page.open_product_card_by_index(index=6)
        product_page.check_loaded()

        product2 = product_page.add_product_to_cart()

        product_page.header.check_quantity(2)
        product_page.header.open_cart_page()
        cart_page.check_loaded()

        expected_products = [product1, product2]

        cart_page.check_products(expected_products)



    @allure.story(AllureStory.DELETE_PRODUCT)
    @allure.title("Удаление одного из двух товаров из корзины")
    @pytest.mark.regression
    def test_delete_one_of_two_products(self, cart_two_product: CartPage):
        cart_page, product1, product2 = cart_two_product

        cart_page.delete_item_by_articul(product1['articul'])

        cart_page.header.check_quantity(1)
        cart_page.check_products([product2])

        cart_page.check_total_quantity()

    @allure.story(AllureStory.CHANGE_QUANTITY)
    @allure.title("Увеличение количества одного товара не изменяет второй товар")
    @pytest.mark.regression
    def test_plus_quantity_first_product_not_affect_second(self, cart_two_product: CartPage):
        cart_page, product1, product2 = cart_two_product

        cart_page.plus_quantity_by_articul(product1['articul'])
        cart_page.check_quantity_by_articul(product1["articul"], 2)

        cart_page.check_added_product_by_articul(product2)
        cart_page.header.check_quantity(3)
        cart_page.check_total_quantity()



    @allure.story(AllureStory.CART_PRICE)
    @allure.title("Пересчет общей стоимости корзины после увеличения количества одного из двух товаров")
    @pytest.mark.regression
    def test_cart_price_after_plus_quantity_with_two_products(self, cart_two_product: CartPage):
        cart_page, product1, product2 = cart_two_product

        cart_page.plus_quantity_by_articul(product1['articul'])
        expected = (product1["price"] *2 + product2["price"])

        cart_page.check_total_price(expected)



    def test_cart_save_after_refresh(self, cart_two_product: CartPage):
        cart_page, product1, product2 = cart_two_product

        cart_page.reload()
        cart_page.check_loaded()

        cart_page.check_products([product1, product2])

        cart_page.header.check_quantity(2)
        cart_page.check_total_quantity()




    @allure.story(AllureStory.DELETE_PRODUCT)
    @allure.title('Удаление товара из корзины')
    @pytest.mark.smoke
    def test_delete_product_from_cart(self, cart_one_product: CartPage):
        cart_one_product.delete_item(index=0)

        cart_one_product.check_cart_is_empty()
        cart_one_product.check_current_url()



    @allure.story(AllureStory.CHANGE_QUANTITY)
    @allure.title("Увеличение количества товара в корзине")
    @pytest.mark.regression
    def test_plus_product_quantity(self, cart_one_product: CartPage):

        old_quantity = cart_one_product.get_item_quantity(0)
        old_header_cart_count = cart_one_product.header.get_num_cart()

        cart_one_product.plus_quantity_item(0, 1)

        cart_one_product.check_item_quantity(0, old_quantity + 1)
        cart_one_product.header.check_quantity(old_header_cart_count + 1)




    @allure.story(AllureStory.CHANGE_QUANTITY)
    @allure.title("Уменьшение количества товара в корзине")
    @pytest.mark.regression
    def test_minus_product_quantity(self, cart_two_quantity: CartPage):

        old_quantity = cart_two_quantity.get_item_quantity(0)

        old_num_cart_header = cart_two_quantity.header.get_num_cart()

        cart_two_quantity.minus_quantity_item(0, 1)
        cart_two_quantity.check_item_quantity(0, old_quantity - 1)
        cart_two_quantity.header.check_quantity(old_num_cart_header - 1)




    @allure.story(AllureStory.CART_PRICE)
    @allure.title("Пересчет итоговой стоимости корзины после увеличения количества товара на 1")
    @pytest.mark.regression
    def test_cart_price_after_plus_1_quantity(self, cart_one_product: CartPage):

        product= cart_one_product.get_product_info(index=0)
        old_total_price = cart_one_product.summary.get_total_price()

        cart_one_product.plus_quantity_item(index=0)
        cart_one_product.check_item_quantity(0, product['quantity'] + 1)

        cart_one_product.check_total_price(old_total_price + product['price'])
        cart_one_product.check_total_quantity()



    @allure.story(AllureStory.CART_PRICE)
    @allure.title("Пересчет итоговой стоимости корзины после уменьшения количества товара на 1")
    @pytest.mark.regression
    def test_cart_price_after_minus_1_quantity(self, cart_two_quantity: CartPage):

        product= cart_two_quantity.get_product_info(index=0)
        old_total_price = cart_two_quantity.summary.get_total_price()

        cart_two_quantity.minus_quantity_item(index=0)
        cart_two_quantity.check_item_quantity(0, product['quantity'] - 1)

        cart_two_quantity.check_total_price(old_total_price - (product['price'] / 2))
        cart_two_quantity.check_total_quantity()











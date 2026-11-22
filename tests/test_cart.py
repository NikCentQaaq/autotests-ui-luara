import allure
import pytest

from pages.cart_page import CartPage
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
        opened_product.size.select_size_if_needed()

        product = opened_product.get_product_info()

        opened_product.click_add_button()

        opened_product.check_popup_success_add()
        opened_product.check_num_cart_into_header(1)

        opened_product.header.open_cart_page()
        cart_page.check_loaded()

        cart_page.check_added_product(product=product)



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











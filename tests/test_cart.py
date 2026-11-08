
import allure
import pytest

from pages.cart_page import CartPage
from pages.product_page import ProductPage


class TestCart:

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

        opened_product.check_current_url()

        opened_product.size.select_size_if_needed()
        product = opened_product.get_product_info()

        opened_product.add_product_to_cart()

        opened_product.check_popup_success_add()
        opened_product.check_num_cart_into_header(1)

        opened_product.header.open_cart()

        cart_page.check_current_url()
        cart_page.check_elements()

        cart_page.check_name_item(0, product["name"])
        cart_page.check_size_item(0, product["size"])
        cart_page.check_articul_item(0, product["articul"])
        cart_page.check_total_quantity()

        cart_page.check_total_price(product["price"])
        cart_page.check_item_quantity(0, 1)


    def test_delete_product_from_cart(self, opened_cart_with_1_product: CartPage):

        opened_cart_with_1_product.delete_item(0)

        opened_cart_with_1_product.check_cart_is_empty()












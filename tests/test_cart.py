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
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_add_1_product_to_cart(self, opened_product: ProductPage, cart_page: CartPage):

        opened_product.check_current_url()

        opened_product.size.select_size_if_needed()

        product = opened_product.get_product_info()

        opened_product.add_product_to_cart()

        opened_product.check_popup_success_add()
        opened_product.check_num_cart_into_header(1)

        opened_product.header.open_cart_page()

        cart_page.check_current_url()
        cart_page.check_elements()

        cart_page.check_name_item(0, product["name"])
        if product["size"]:
            cart_page.check_size_item(0, product["size"])
        cart_page.check_articul_item(0, product["articul"])
        cart_page.check_total_quantity()

        cart_page.check_total_price(product["price_quantity"])
        cart_page.check_item_quantity(0, 1)

    @allure.title('Удаление товара из корзины')
    @pytest.mark.smoke
    def test_delete_product_from_cart(self, cart_with_1_product: CartPage):

        cart_with_1_product.delete_item(index=0)

        cart_with_1_product.check_cart_is_empty()



    @allure.title("Увеличение количества товара в корзине")
    @pytest.mark.smoke
    def test_plus_product_quantity(self, cart_with_1_product: CartPage):

        old_quantity = cart_with_1_product.get_item_quantity(0)
        old_header_cart_count = cart_with_1_product.header.get_num_cart()

        cart_with_1_product.plus_quantity_item(0, 1)

        cart_with_1_product.check_item_quantity(0, old_quantity + 1)
        cart_with_1_product.header.check_quantity(old_header_cart_count + 1)




    @allure.title("Уменьшение количества товара в корзине")
    @pytest.mark.smoke
    def test_minus_product_quantity(self, cart_with_2_items_products: CartPage):

        old_quantity = cart_with_2_items_products.get_item_quantity(0)

        old_num_cart_header = cart_with_2_items_products.header.get_num_cart()

        cart_with_2_items_products.minus_quantity_item(0, 1)
        cart_with_2_items_products.check_item_quantity(0, old_quantity - 1)
        cart_with_2_items_products.header.check_quantity(old_num_cart_header - 1)



    @allure.title("Пересчет итоговой стоимости корзины после увеличения количества товара на 1")
    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_cart_price_after_plus_1_quantity(self, cart_with_1_product: CartPage):

        product= cart_with_1_product.get_product_info(index=0)
        old_total_price = cart_with_1_product.summary.get_total_price()

        cart_with_1_product.plus_quantity_item(index=0)
        cart_with_1_product.check_item_quantity(0, product['quantity'] + 1)

        cart_with_1_product.check_total_price(old_total_price + product['price'])
        cart_with_1_product.check_total_quantity()



    @allure.title("Пересчет итоговой стоимости корзины после уменьшения количества товара на 1")
    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_cart_price_after_minus_1_quantity(self, cart_with_2_items_products: CartPage):

        product= cart_with_2_items_products.get_product_info(index=0)
        old_total_price = cart_with_2_items_products.summary.get_total_price()

        cart_with_2_items_products.minus_quantity_item(index=0)
        cart_with_2_items_products.check_item_quantity(0, product['quantity'] - 1)

        cart_with_2_items_products.check_total_price(old_total_price - (product['price'] / 2))
        cart_with_2_items_products.check_total_quantity()











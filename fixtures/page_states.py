import re
import pytest

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@pytest.fixture
def opened_catalog_page(catalog_page: CatalogPage):

    catalog_page.open()
    catalog_page.check_current_url()
    catalog_page.check_elements_without_filter()
    return catalog_page

@pytest.fixture
def opened_main_page(main_page: MainPage):
    main_page.open()
    main_page.check_current_url_expected(re.compile(r"luara-art\.ru"))
    main_page.check_elements()
    return main_page




@pytest.fixture
def opened_product(
        request,
        opened_catalog_page: CatalogPage,
        product_page: ProductPage
):
    index = request.param

    opened_catalog_page.open_product_card_by_index(index)
    product_page.check_current_url()
    return product_page



@pytest.fixture
def cart_with_1_product(
    opened_catalog_page: CatalogPage,
    product_page: ProductPage,
    cart_page: CartPage,
):
    opened_catalog_page.open_product_card_random()

    product_page.check_current_url()
    product_page.check_elements()

    product_page.size.select_size_if_needed()

    product_page.add_product_to_cart()
    product_page.check_popup_success_add()
    product_page.check_num_cart_into_header(1)

    product_page.header.open_cart()

    cart_page.check_current_url()
    cart_page.wait_items_loaded()
    cart_page.check_elements()

    return cart_page



@pytest.fixture
def cart_with_2_items_products(cart_with_1_product: CartPage):

    cart_with_1_product.plus_quantity_item(0)

    cart_with_1_product.check_item_quantity(0, 2)
    cart_with_1_product.header.check_quantity(2)

    return cart_with_1_product



@pytest.fixture
def opened_search_page(opened_main_page: MainPage  ,search_page: SearchPage):
    opened_main_page.header.search('Браслет')

    search_page.check_current_url()
    search_page.check_elements()
    search_page.check_search_results_by_name('Браслет')

    return search_page








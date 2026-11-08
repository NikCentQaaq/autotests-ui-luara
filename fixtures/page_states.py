import re
import pytest

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


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
def opened_cart_with_1_product(
    opened_catalog_page: CatalogPage,
    product_page: ProductPage,
    cart_page: CartPage,
):
    opened_catalog_page.open_product_card_random()

    product_page.check_current_url()
    product_page.check_elements()

    product_page.size.select_size_if_needed()

    product_page.add_product_to_cart()

    product_page.header.open_cart()

    cart_page.check_current_url()
    cart_page.check_elements()

    return cart_page


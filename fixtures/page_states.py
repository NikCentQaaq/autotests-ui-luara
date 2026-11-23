import pytest

from config import settings
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@pytest.fixture
def opened_catalog_page(catalog_page: CatalogPage):

    catalog_page.open()
    catalog_page.check_loaded_without_filter()
    return catalog_page

@pytest.fixture
def opened_main_page(main_page: MainPage):
    main_page.open()
    main_page.check_loaded()
    return main_page


@pytest.fixture
def opened_product(
        request,
        opened_catalog_page: CatalogPage,
        product_page: ProductPage
):
    index = getattr(request, "param", 11)
    opened_catalog_page.open_product_card_by_index(index)

    product_page.check_loaded()
    return product_page


@pytest.fixture
def cart_one_product(opened_product: ProductPage, cart_page: CartPage):

    opened_product.add_product_to_cart()

    opened_product.header.check_quantity(1)
    opened_product.header.open_cart_page()

    cart_page.check_loaded()

    return cart_page



@pytest.fixture
def cart_two_quantity(cart_one_product: CartPage):

    cart_one_product.plus_quantity_item(0)

    cart_one_product.check_item_quantity(0, 2)
    cart_one_product.header.check_quantity(2)

    return cart_one_product



@pytest.fixture
def search_results_page(request,
        opened_main_page: MainPage,
        search_page: SearchPage
    ):
    text = getattr(request, "param", "Браслет")

    opened_main_page.header.search(text)

    search_page.check_loaded()
    search_page.check_search_results_by_name(text)
    return search_page



@pytest.fixture
def opened_login_page(login_page: LoginPage):
    login_page.open()
    login_page.check_loaded()
    return login_page


@pytest.fixture
def opened_personal_page(opened_login_page: LoginPage, personal_page: PersonalPage):
    opened_login_page.fill_login_form(login=settings.test_user.login, password=settings.test_user.password)

    personal_page.check_loaded()
    return personal_page


@pytest.fixture
def cart_two_product(opened_product: ProductPage, opened_catalog_page: CatalogPage, cart_page: CartPage):

    product1 = opened_product.add_product_to_cart()

    opened_product.back_to_catalog_page()

    opened_catalog_page.open_product_card_by_index(index=5)
    opened_product.check_loaded()

    product2 = opened_product.add_product_to_cart()

    opened_product.header.check_quantity(2)
    opened_product.header.open_cart_page()

    cart_page.wait_items_loaded()
    cart_page.check_loaded()

    return cart_page, product1, product2












import pytest
from playwright.sync_api import Page

from pages.aktsii_page import AktsiiPage
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.magazines_page import MagazinesPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@pytest.fixture
def main_page(page: Page) -> MainPage:
    return MainPage(page=page)

@pytest.fixture
def catalog_page(page: Page) -> CatalogPage:
    return CatalogPage(page=page)


@pytest.fixture
def product_page(page: Page) -> ProductPage:
    return ProductPage(page=page)

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page=page)

@pytest.fixture
def search_page(page: Page) -> SearchPage:
    return SearchPage(page=page)

@pytest.fixture
def aktsii_page(page: Page) -> AktsiiPage:
    return AktsiiPage(page=page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

@pytest.fixture
def magazines_page(page: Page) -> MagazinesPage:
    return MagazinesPage(page=page)

@pytest.fixture
def personal_page(page: Page) -> PersonalPage:
    return PersonalPage(page=page)





import allure
import pytest

from pages.aktsii_page import AktsiiPage
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.magazines_page import MagazinesPage
from pages.main_page import MainPage


class TestHeaderNavigation:

    @allure.title("Отображение всех элементов Шапки сайта")
    def test_header_elements(self, opened_main_page: MainPage):
        opened_main_page.header.top_header.check_elements()
        opened_main_page.header.middle_header.check_elements()
        opened_main_page.header.top_panel.check_elements()




    @allure.title("Переход на главную страницу по логотипу")
    def test_open_main_page_from_header_logo(self, opened_catalog_page: CatalogPage, main_page: MainPage):
        opened_catalog_page.header.open_main_page()

        main_page.check_current_url()
        main_page.check_elements()



    @allure.title("Переход в корзину")
    @pytest.mark.regression
    def test_open_cart_page(self, opened_main_page: MainPage,cart_page: CartPage):
        opened_main_page.header.open_cart_page()

        cart_page.check_current_url()
        cart_page.check_cart_is_empty()


    @allure.title("Переход на страницу авторизации")
    @pytest.mark.regression
    def test_open_login_page(self, opened_main_page: MainPage, login_page: LoginPage):
        opened_main_page.header.open_login_page()

        login_page.check_current_url()
        login_page.check_elements()



    @allure.title("Переход на страницу акций")
    @pytest.mark.regression
    def test_open_aktsii_page(self, opened_main_page: MainPage, aktsii_page: AktsiiPage):
        opened_main_page.header.open_aktsii_page()

        aktsii_page.check_current_url()
        aktsii_page.check_elements()



    @allure.title("Переход на страницу магазинов")
    @pytest.mark.regression
    def test_open_magazines_page(self, opened_main_page: MainPage, magazines_page: MagazinesPage):
        opened_main_page.header.open_magazines_page()

        magazines_page.check_current_url()
        magazines_page.check_elements()













    # @pytest.mark.parametrize("open_method, expected_page",
    # [pytest.param(HeaderComponent.open_main_page, MainPage, id="main_page"),
    #  pytest.param(HeaderComponent.open_cart_page, CartPage, id="cart_page"),
    #  pytest.param(HeaderComponent.open_login_page, LoginPage, id="login_page"),
    #  pytest.param(HeaderComponent.open_aktsii_page, AktsiiPage, id="aktsii_page"),
    #  pytest.param(HeaderComponent.open_magazines_page, MagazinesPage, id="magazines_page")
    # ])
    # def test_navig(self, open_method,  expected_page: BasePage, opened_main_page: MainPage):
    #
    #     open_method(opened_main_page.header)
    #     page = expected_page(opened_main_page.page)
    #     page.check_current_url()
    #     page.check_elements()








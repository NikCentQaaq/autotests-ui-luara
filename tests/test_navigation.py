import allure
import pytest

from fixtures.pages import main_page
from pages.main_page import MainPage
from pages.product_page import ProductPage


class TestHeaderNavigation:

    @allure.title("Переход на главную страницу по логотипу")
    @pytest.mark.parametrize("opened_product",
        [pytest.param(1, id="product_2"),
        pytest.param(10, id="product_11")],
                             indirect=True)
    def test_open_main_page_from_header_logo(self, opened_product: ProductPage, main_page: MainPage):

        opened_product.header.open_main_page()

        main_page.check_current_url()
        main_page.check_elements()



    # main  login kontakty magazines
    # def test_navig(self):
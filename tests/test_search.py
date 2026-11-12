import allure
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestSearch:


    @allure.title("Поиск товара по артикулу с главной страницы")
    @pytest.mark.parametrize('value', [
        pytest.param('BE19907', id='base', marks=pytest.mark.smoke),
        pytest.param('BE19907-2', id='base', marks=pytest.mark.regression),
        pytest.param('be19907-2', id='lowercase', marks=pytest.mark.regression)
    ])
    def test_search_by_articul(self, value,opened_main_page: MainPage, search_page: SearchPage):

        opened_main_page.header.search(value)

        search_page.check_current_url()
        search_page.check_elements()

        search_page.check_search_results_by_articul(value)





    @allure.title("Поиск товара по названию с главной страницы")
    @pytest.mark.parametrize('value, value_product', [
        pytest.param('Кольцо', 'Кольцо', id='base', marks=pytest.mark.smoke),
        pytest.param('КОЛЬЦО', 'КОЛЬЦО', id='uppercase', marks=pytest.mark.regression),
        pytest.param('кольцо', 'кольцо', id='lowercase', marks=pytest.mark.regression),
        pytest.param('кольца', 'кольцо', id='plural', marks=pytest.mark.regression),
        pytest.param('кольц', 'кольцо', id='partial', marks=pytest.mark.regression),
        pytest.param('кольцо"', 'кольцо', id='partial', marks=pytest.mark.regression)
    ])
    def test_search_by_name(self, value, value_product: str, opened_main_page: MainPage, search_page: SearchPage):

        opened_main_page.header.search(value)

        search_page.check_current_url()
        search_page.check_elements()

        search_page.check_search_results_by_name(value_product)




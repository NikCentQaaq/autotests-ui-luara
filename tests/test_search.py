import allure
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from tools.enums.allure_enum import AllureEpic, AllureFeature, AllureStory


@allure.epic(AllureEpic.UI)
@allure.feature(AllureFeature.SEARCH)

class TestSearch:

    @allure.story(AllureStory.SEARCH)
    @allure.title("Поиск товара по артикулу с главной страницы")
    @pytest.mark.parametrize('value', [
        pytest.param('BE19907', id='base', marks=pytest.mark.smoke),
        pytest.param('BE19907-2', id='base', marks=pytest.mark.regression),
        pytest.param('be19907-2', id='lowercase', marks=pytest.mark.regression)
    ])
    def test_search_by_articul(self, value,opened_main_page: MainPage, search_page: SearchPage):

        opened_main_page.header.search(value)

        search_page.check_loaded()

        search_page.check_search_results_by_articul(value)

    @allure.story(AllureStory.SEARCH)
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

        search_page.check_loaded()

        search_page.check_search_results_by_name(value_product)



    @pytest.mark.regression
    @pytest.mark.negative
    @allure.title('Поиск по запросу без результатов')
    @pytest.mark.parametrize('value', [
        pytest.param('', id='empty search'),
        pytest.param('кольфв', id='invalid search'),
        pytest.param('!@#$', id='special symbols'),
        pytest.param('💍', id='emoji'),
        pytest.param('кольцо'*20, id='long string')
    ])
    def test_search_with_no_results(self, value, opened_main_page: MainPage, search_page: SearchPage):
        opened_main_page.header.search(value)
        search_page.check_current_url()
        search_page.check_no_search_results()







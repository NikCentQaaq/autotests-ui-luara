import allure
import pytest

from pages.catalog_page import CatalogPage
from tools.enums.allure_enum import AllureStory


class TestFilterCatalog:


    # def test_filter_price_catalog(self, opened_catalog_page: CatalogPage):
    #     opened_catalog_page.filter.search.search('Кольца')



    @allure.story(AllureStory.FILTER)
    @allure.title("Фильтрация по диапазону цен")
    @pytest.mark.parametrize("min_price, max_price", [
        pytest.param(10000, 50000, id='base', marks=pytest.mark.smoke),
        pytest.param(0, 60000, id='min 0', marks=pytest.mark.regression),
        pytest.param(9990, 9990, id='equal_min_max', marks=pytest.mark.regression),
        pytest.param(2500000, 2690000, id='most_expensive_product', marks=pytest.mark.regression)])
    def test_filter_price(self, min_price: int, max_price: int,  opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.fill_price_range(min_price, max_price)

        opened_catalog_page.filter.check_result()
        opened_catalog_page.filter.click_show_result()

        opened_catalog_page.check_price_filter_url(min_price, max_price)
        opened_catalog_page.check_title(f'цена от {min_price} до {max_price}')
        opened_catalog_page.check_range_prices(min_price, max_price)



    @allure.story(AllureStory.FILTER)
    @allure.title("Негативные сценарии. Фильтрация по диапазону цен")
    @pytest.mark.parametrize("min_price, max_price", [
        pytest.param(10000, 50000, id='base', marks=[pytest.mark.regression, pytest.mark.negative]),
        pytest.param(0, 60000, id='min 0', marks=[pytest.mark.regression, pytest.mark.negative]),
        pytest.param(9990, 9990, id='equal_min_max', marks=[pytest.mark.regression, pytest.mark.negative]),
        pytest.param(2500000, 2690000, id='most_expensive_product', marks=[pytest.mark.regression, pytest.mark.negative])])
    def test_negative_filter_price(self, min_price: int, max_price: int,  opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.fill_price_range(min_price, max_price)

        opened_catalog_page.filter.check_result()
        opened_catalog_page.filter.click_show_result()

        opened_catalog_page.check_price_filter_url(min_price, max_price)
        opened_catalog_page.check_title(f'цена от {min_price} до {max_price}')
        opened_catalog_page.check_range_prices(min_price, max_price)


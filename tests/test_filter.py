import allure
import pytest

from pages.catalog_page import CatalogPage
from tools.enums.allure_enum import AllureStory, AllureEpic, AllureFeature
from tools.enums.category import Metall


@allure.epic(AllureEpic.UI)
@allure.feature(AllureFeature.FILTER)
class TestFilterCatalog:


    # def test_filter_price_catalog(self, opened_catalog_page: CatalogPage):
    #     opened_catalog_page.filter.search.search('Кольца')



    @allure.story(AllureStory.PRICE_FILTER)
    @allure.title("Фильтрация по диапазону цен")
    @pytest.mark.parametrize("min_price, max_price", [
        pytest.param(10000, 50000, id='base', marks=pytest.mark.smoke),
        pytest.param(0, 60000, id='min 0', marks=pytest.mark.regression),

        pytest.param(9990, 9990, id='equal_min_max', marks=pytest.mark.regression),
        pytest.param(2500000, 2690000, id='most_expensive_product', marks=pytest.mark.regression)])
    def test_filter_price(self, min_price: int, max_price: int,  opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.fill_price_range(min_price, max_price)

        opened_catalog_page.filter.check_result_count()
        opened_catalog_page.filter.click_show_result()

        opened_catalog_page.check_price_filter_url(min_price, max_price)
        opened_catalog_page.check_title(f'цена от {min_price} до {max_price}')
        opened_catalog_page.check_range_prices(min_price, max_price)



    @allure.story(AllureStory.PRICE_FILTER)
    @allure.title("Фильтрация по диапазону цен без результатов")
    @allure.description("Проверка отображения пустого каталога при выборе диапазона цен, для которого отсутствуют товары.")
    @pytest.mark.regression
    @pytest.mark.negative
    @pytest.mark.parametrize("min_price, max_price", [
        pytest.param('2690001', '2690001', id='above_max_price'),
        pytest.param('', '1899', id='less_min_prise'),
        pytest.param('50991', '54899', id='dont_exist_prise'),
        pytest.param('10000', '5000', id='min_is_greater_than_max')
    ])
    def test_filter_price_no_results(self, min_price: int, max_price: int,  opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.fill_price_range(min_price, max_price)

        opened_catalog_page.filter.check_results_count_zero()
        opened_catalog_page.filter.click_show_result()

        opened_catalog_page.check_cards_count(0)


    @allure.story(AllureStory.PRICE_FILTER)
    @allure.title("Ввод некорректных символов в поле 'Цена от'")
    @pytest.mark.regression
    @pytest.mark.negative
    @pytest.mark.xfail(reason='Известная проблема: отсутствует валидация нечислового ввода в поле "Цена от"')
    @pytest.mark.parametrize("min_price", [
        pytest.param('фыва', id='cyrillic'),
        pytest.param('!!!!', id='special_chars'),
        pytest.param('abc', id='latin'),
        pytest.param('1фис345', id='mixed')
    ])
    def test_min_price_filter_invalid_input(self, min_price: int, opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.price.fill_min_price(min_price)
        opened_catalog_page.filter.click_show_result()
        opened_catalog_page.filter.price.check_min_price('')




    @allure.story(AllureStory.PRICE_FILTER)
    @allure.title("Ввод некорректных символов в поле 'Цена до'")
    @pytest.mark.regression
    @pytest.mark.negative
    @pytest.mark.xfail(reason='Известная проблема: отсутствует валидация нечислового ввода в поле "Цена до"')
    @pytest.mark.parametrize("max_price", [
        pytest.param('фыва', id='cyrillic'),
        pytest.param('!!!!', id='special_chars'),
        pytest.param('abc', id='latin'),
        pytest.param('1фис345', id='mixed')
    ])
    def test_max_price_filter_invalid_input(self, max_price: int, opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.price.fill_max_price(max_price)
        opened_catalog_page.filter.click_show_result()
        opened_catalog_page.filter.price.check_max_price('')







    @allure.story(AllureStory.METALL_FILTER)
    @allure.title("Фильтрация по металлу изделий")
    @pytest.mark.parametrize("metall, text_value, url", [
        pytest.param(Metall.SILVER, 'серебр', Metall.SILVER.url_pattern, id='silver',marks=pytest.mark.smoke),
        pytest.param(Metall.GOLD, 'золот', Metall.GOLD.url_pattern, id='gold', marks=pytest.mark.regression),
        pytest.param(Metall.JEWELRY_ALLOY, '', Metall.JEWELRY_ALLOY.url_pattern, id='bijuteria', marks=pytest.mark.regression)])
    def test_select_metall(self, metall: Metall, text_value:str , url: str, opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.select_metall(metall)

        opened_catalog_page.filter.check_result_count()
        opened_catalog_page.filter.click_show_result()

        opened_catalog_page.check_current_url_expected(url)
        opened_catalog_page.check_names_contain_text(text_value)












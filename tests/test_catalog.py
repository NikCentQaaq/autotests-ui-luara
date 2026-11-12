import re
import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from tools.enums.category import Category
from tools.enums.routes import UrlPattern
from tools.enums.sort_type import SortType


class TestCatalog:

    @allure.title('Открытие категории через блок каталога на главной странице')
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "catalog_category, product_category",
        [pytest.param(Category.RINGS,Category.RING,id="rings"),
        pytest.param(Category.EARRINGS,Category.EARRINGS,id="earrings"),
        pytest.param(Category.BRACELETS,Category.BRACELET, id="bracelets"),
        pytest.param(Category.NECKLACES,    Category.NECKLACES, id="necklaces"),
        pytest.param( Category.PENDANTS,Category.PENDANT,id="pendants")
        ]
    )
    def test_open_category_from_concern_catalog(
            self,
            opened_main_page: MainPage,
            catalog_page: CatalogPage,
            catalog_category: Category,
            product_category: Category
    ):

        opened_main_page.open_category(catalog_category)

        catalog_page.check_current_url()
        catalog_page.check_elements_filter_products()

        catalog_page.check_selected_filter(catalog_category)
        catalog_page.check_products_category(product_category)





    @pytest.mark.regression
    @allure.title('Сортировка продуктов в Каталоге')
    @pytest.mark.parametrize(
        "sort_type",
        [pytest.param(SortType.POPULAR,id="POPULAR"),
        pytest.param(SortType.COMPLETENESS,id="COMPLETENESS"),
        pytest.param(SortType.PRICE_ASC,id="PRICE_ASC"),
        pytest.param( SortType.PRICE_DESC,id="PRICE_DESC")
    ])
    def test_sort_products(self, sort_type:SortType, opened_catalog_page: CatalogPage):

        opened_catalog_page.sort_products_by_value(sort_type)
        opened_catalog_page.check_current_url()



    @allure.title("Сортировка товаров по цене")
    @pytest.mark.regression
    @pytest.mark.xfail(reason="BUG: Некорректная сортировка товаров по цене на сайте")
    @pytest.mark.parametrize('sort_type, url',
        [pytest.param(SortType.PRICE_ASC,UrlPattern.PRICE_ASC, id="PRICE_ASC"),
         pytest.param(SortType.PRICE_DESC,UrlPattern.PRICE_DESC, id="PRICE_DESC")
    ])
    def test_sort_price(self, sort_type:SortType, url: UrlPattern, opened_catalog_page: CatalogPage):
        opened_catalog_page.sort_products_by_value(sort_type)
        opened_catalog_page.check_current_url_expected(re.compile(url))

        if sort_type == SortType.PRICE_ASC:
            opened_catalog_page.check_prices_sorted_asc()
        else:
            opened_catalog_page.check_prices_sorted_desc()




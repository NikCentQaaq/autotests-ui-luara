import re

import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from tools.enums.category import Category
from tools.enums.sort_type import SortType


class TestCatalog:

    @allure.title('Открытие категории через блок каталога на главной странице')
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "catalog_category, product_category",
        [(Category.RINGS, Category.RING),
         (Category.EARRINGS, Category.EARRINGS),
         (Category.BRACELETS, Category.BRACELET),
         (Category.NECKLACES, Category.NECKLACES),
         (Category.PENDANTS, Category.PENDANT)],
        ids=[
            "rings",
            "earrings",
            "bracelets",
            "necklaces",
            "pendants",
        ]
    )
    def test_open_category_from_concern_catalog(
            self, main_page: MainPage,
            catalog_page: CatalogPage,
            catalog_category: Category,
            product_category: Category
    ):
        main_page.open()
        main_page.check_current_url(re.compile(r"luara-art\.ru"))

        main_page.open_category(catalog_category)

        catalog_page.check_current_url(re.compile(r".*catalog/.*"))
        catalog_page.check_elements_filter_products()

        catalog_page.check_selected_filter(catalog_category)
        catalog_page.check_products_category(product_category)




    @pytest.mark.smoke
    @allure.title('Сортировка продуктов в Каталоге')
    @pytest.mark.parametrize("sort_type",
    (SortType.POPULAR,
     SortType.COMPLETENESS,
     SortType.PRICE_ASC,
     SortType.PRICE_DESC),
            ids=["по популярности", "по комплектности", "по убыванию цены", "по возрастанию цены"])
    def test_sort_products(self, sort_type:SortType, catalog_page: CatalogPage):

        catalog_page.open()

        catalog_page.check_current_url(re.compile(r".*catalog.*"))
        catalog_page.check_elements_without_filter()

        catalog_page.sort_products_by_value(sort_type)
        catalog_page.check_current_url(re.compile(sort_type.url))




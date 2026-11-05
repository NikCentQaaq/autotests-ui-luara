import re

import allure
import pytest

from config import settings
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from tools.enums.category import Category


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
        main_page.open(settings.get_base_url())
        main_page.check_current_url(re.compile(r"luara-art\.ru"))

        main_page.open_category(catalog_category)

        catalog_page.check_current_url(re.compile(r".*catalog/.*"))
        catalog_page.check_elements()

        catalog_page.check_selected_filter(catalog_category)
        catalog_page.check_products_category(product_category)



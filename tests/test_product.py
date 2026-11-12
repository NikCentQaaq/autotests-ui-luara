import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from tools.enums.category import Category


class TestProduct:

    @allure.title("Открытие карточки товара из каталога")
    @pytest.mark.smoke
    @pytest.mark.parametrize("index", (1, 10))
    def test_open_product_from_catalog(self, index: int, opened_catalog_page: CatalogPage, product_page: ProductPage):

        opened_catalog_page.open_product_card_by_index(index)

        product_page.check_current_url()
        product_page.check_elements()


    @allure.title("Открытие карточки товара из результатов Поиска")
    @pytest.mark.smoke
    def test_open_product_from_search(self, opened_search_page: SearchPage, product_page: ProductPage):
        opened_search_page.open_product_card_by_index(0)

        product_page.check_current_url()
        product_page.check_elements()












    @allure.title("Открытие товара из выбранной категории")
    @pytest.mark.parametrize(
        "catalog_category, product_category",[
            pytest.param(Category.RINGS,Category.RING,
                id="rings",  marks=pytest.mark.smoke
            ),
            pytest.param( Category.EARRINGS,Category.EARRINGS,
                id="earrings", marks=pytest.mark.regression
            ),
            pytest.param(Category.BRACELETS,Category.BRACELET,
                id="bracelets", marks=pytest.mark.regression
            ),
            pytest.param(Category.NECKLACES,Category.NECKLACES,
                id="necklaces", marks=pytest.mark.regression
            ),
            pytest.param(Category.PENDANTS,Category.PENDANT,
                id="pendants", marks=pytest.mark.regression
            ),
        ],
    )
    def test_open_product_from_category(
            self,
            opened_main_page: MainPage,
            catalog_page: CatalogPage,
            product_page: ProductPage,
            catalog_category: Category,
            product_category: Category
    ):
        opened_main_page.open_category(catalog_category)

        catalog_page.open_product_card_random()

        product_page.check_current_url()
        product_page.check_elements()
        product_page.check_name_have_category(product_category)







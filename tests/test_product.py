import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage



class TestProduct:

    @allure.title("Открытие карточки товара из каталога")
    @pytest.mark.smoke
    @pytest.mark.parametrize("index", (1, 10))
    def test_open_product_from_catalog(self, index: int, opened_catalog_page: CatalogPage, product_page: ProductPage):

        opened_catalog_page.open_product_card_by_index(index)

        product_page.check_current_url()
        product_page.check_elements()









    # @allure.title("Открытие карточки товара из каталога")
    # @pytest.mark.smoke
    # @pytest.mark.parametrize(
    #     "catalog_category, product_category",
    #     [(Category.RINGS, Category.RING),
    #      (Category.EARRINGS, Category.EARRINGS),
    #      (Category.BRACELETS, Category.BRACELET),
    #      (Category.NECKLACES, Category.NECKLACES),
    #      (Category.PENDANTS, Category.PENDANT)],
    #     ids=[
    #         "rings",
    #         "earrings",
    #         "bracelets",
    #         "necklaces",
    #         "pendants",
    #     ]
    # )
    # def test_open_product_from_catalog_FULL(
    #         self,
    #         main_page: MainPage,
    #         catalog_page: CatalogPage,
    #         product_page: ProductPage,
    #         catalog_category: Category,
    #         product_category: Category
    # ):
    #
    #     main_page.open(settings.get_base_url())
    #     main_page.check_current_url(re.compile(r"luara-art\.ru"))
    #
    #     main_page.open_category(catalog_category)
    #
    #     catalog_page.check_current_url(re.compile(r".*catalog/.*"))
    #     catalog_page.check_elements()
    #
    #     catalog_page.open_product_card_by_index(1)
    #
    #     product_page.check_current_url(re.compile(r".*catalog/product/.*"))
    #     product_page.check_elements()
    #
    #     product_page.check_catalog_header(catalog_category)
    #     product_page.check_name_have_category(product_category)







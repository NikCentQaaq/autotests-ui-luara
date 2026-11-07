import re

from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
#
#
# class TestCart:
#
#     def test_add_product_to_cart(self, catalog_page: CatalogPage, product_page: ProductPage):
#
#         catalog_page.open()
#         catalog_page.check_current_url(re.compile(r".*catalog.*"))
#         catalog_page.check_elements_without_filter()
#
#         catalog_page.open_product_card_by_index(1)
#         product_page.check_current_url(re.compile(r".*catalog/product/.*"))
#
#         name_product = product_page.get_product_name()
#         price_product = product_page.get_product_price()
#         selected_size = product_page.add_product_to_cart()
#
#         product_page.check_popup_success_add()
#         product_page.check_num_cart_into_header(1)







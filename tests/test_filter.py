from pages.catalog_page import CatalogPage


class TestFilterCatalog:


    def test_filter_price_catalog(self, opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.search.search('Кольца')

    def test_filter_price_catalog_with_filter(self, opened_catalog_page: CatalogPage):
        opened_catalog_page.filter.price.fill_price_range(10000, 1000000)



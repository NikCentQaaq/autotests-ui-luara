
from pages.main_page import MainPage
from config import settings

class TestHomePage:
    def test_home_page_open(self, main_page: MainPage):
        main_page.open(settings.get_base_url())

        main_page.header.check_elements()


import re
import allure
import pytest
from pages.main_page import MainPage




class TestMainPage:

    @pytest.mark.smoke
    @allure.title("Smoke: Проверка главной страницы")
    def test_main_page_smoke(self, main_page: MainPage):
        main_page.open()
        main_page.check_current_url_expected(re.compile(r"luara-art\.ru"))

        main_page.check_elements()

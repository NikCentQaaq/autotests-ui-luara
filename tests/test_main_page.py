import re
import allure
import pytest

from pages.main_page import MainPage
from config import settings



class TestMainPage:

    @pytest.mark.smoke
    @allure.title("Smoke: Проверка главной страницы")
    def test_main_page_smoke(self, main_page: MainPage):
        main_page.open(settings.get_base_url())
        main_page.check_current_url(re.compile(r"luara-art\.ru"))

        main_page.check_elements()

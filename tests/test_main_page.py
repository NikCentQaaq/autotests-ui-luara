import re
import allure
import pytest
from pages.main_page import MainPage
from tools.enums.allure_enum import AllureEpic, AllureFeature, AllureStory


@allure.epic(AllureEpic.UI)
@allure.feature(AllureFeature.MAIN_PAGE)
class TestMainPage:

    @allure.story(AllureStory.DISPLAY)
    @pytest.mark.smoke
    @allure.title("Проверка главной страницы")
    def test_main_page_smoke(self, main_page: MainPage):
        main_page.open()
        main_page.check_current_url_expected(re.compile(r"luara-art\.ru"))
        main_page.header.visible_check()

        main_page.check_elements()



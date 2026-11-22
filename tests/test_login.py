import allure
import pytest

from config import settings
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from tools.enums.allure_enum import AllureEpic, AllureFeature, AllureStory


@allure.epic(AllureEpic.UI)
@allure.feature(AllureFeature.AUTHORIZATION)
class TestLogin:

    @allure.story(AllureStory.LOGIN)
    @allure.title('Успешная авторизация')
    @pytest.mark.smoke
    def test_success_login(self, opened_main_page: MainPage, login_page: LoginPage, personal_page: PersonalPage):
        opened_main_page.header.open_login_page()

        login_page.check_current_url()
        login_page.check_elements()

        login_page.fill_login_form(login=settings.test_user.login, password=settings.test_user.password)

        personal_page.check_current_url()
        personal_page.check_elements()




    @allure.story(AllureStory.INVALID_LOGIN)
    @allure.title("Авторизация с некорректными учетными данными")
    @pytest.mark.regression
    @pytest.mark.negative
    @pytest.mark.parametrize('login, password', [
        pytest.param(settings.test_user.login, '12345678', id='wrong password'),
        pytest.param('12345678', settings.test_user.password, id='wrong login and password')])
    def test_invalid_authorization(self, login, password, opened_login_page: LoginPage):

        opened_login_page.fill_login_form(login=login, password=password)

        opened_login_page.check_current_url()
        opened_login_page.check_alert_wrong_data()



    @allure.story(AllureStory.INVALID_LOGIN)
    @allure.title("Авторизация с пустыми обязательными полями")
    @pytest.mark.regression
    @pytest.mark.negative
    @pytest.mark.parametrize('login, password', [
        pytest.param(settings.test_user.login, '', id='empty password'),
        pytest.param('', settings.test_user.password, id='empty login'),
        pytest.param('', '', id='empty login and password')])
    def  test_authorization_with_empty_fields(self, login, password, opened_login_page: LoginPage):
        opened_login_page.fill_login_form(login=login, password=password)

        opened_login_page.check_loaded()



    @allure.story(AllureStory.LOGOUT)
    @allure.title('Успешный выход из личного кабинета с последующим возвратом на главную страницу.')
    @pytest.mark.smoke
    def test_logout(self, opened_personal_page: PersonalPage, main_page: MainPage):
        opened_personal_page.logout()

        main_page.check_loaded()

        main_page.header.check_login_visible()


    @allure.story(AllureStory.LOGOUT)
    @allure.title('Отмена выхода из личного кабинета после нажатия кнопки "Остаться"')
    @pytest.mark.regression
    def test_cancel_logout(self, opened_personal_page: PersonalPage):
        opened_personal_page.stay_after_click_logout()

        opened_personal_page.check_loaded()
        # opened_personal_page.check_elements()

        opened_personal_page.header.check_personal_visible()













from config import settings
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage


class TestLogin:

    def test_success_authentication(self, opened_main_page: MainPage, login_page: LoginPage, personal_page: PersonalPage):
        opened_main_page.header.open_login_page()

        login_page.check_current_url()
        login_page.check_elements()

        login_page.fill_login_form(login=settings.user.login, password=settings.user.password)

        personal_page.check_current_url()
        personal_page.check_elements()








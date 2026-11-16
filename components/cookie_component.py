import allure
from playwright.sync_api import Page



class CookieComponent:

    def __init__(self, page: Page):
        self.accept_button = page.locator("button.coockieMess__accept")

    @allure.step("Принять cookies")
    def accept_if_visible(self):
        if self.accept_button.is_visible(timeout=1000):
            self.accept_button.click()
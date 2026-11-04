from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger('BasePage')

class BasePage:
    def __init__(self, page: Page):
        self.page = page


    def open(self, url: str):
        step = f'Открытие URL {url}'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="load")


    def reload(self):
        step = f'Перезагрузка страницы URL {self.page.url}'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="networkidle")



    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Проверка соответствует ли текущий URL шаблону {expected_url.pattern}'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
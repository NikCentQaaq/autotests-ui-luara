import re
from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from config import settings
from elements.base_element import BaseElement
from tools.enums.routes import Rout
from tools.logger import get_logger

logger = get_logger('BasePage')

class BasePage:

    ROUTE = Rout.MAIN

    def __init__(self, page: Page):
        self.page = page


    def open(self):
        full_url = f"{settings.get_base_url()}{self.ROUTE}"
        step = f'Открытие URL "{full_url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(full_url, wait_until="load")


    def reload(self):
        step = f'Перезагрузка страницы URL {self.page.url}'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="networkidle")



    def check_current_url_expected(self, expected_url: Pattern[str]):
        step = f'Проверка соответствует ли текущий URL шаблону {expected_url.pattern}'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)

    def check_current_url(self):
        step = f'Проверка соответствует ли текущий URL шаблону {self.ROUTE}'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(re.compile(f".*{self.ROUTE}.*"))

    @staticmethod
    def check_element_text_by_name(element: BaseElement):
        step = f'Проверка {element.type_of} "{element.name}"'
        with allure.step(step):
            element.check_visible()
            element.check_have_text(element.name)

    @staticmethod
    def check_element(element: BaseElement, text: str):
        step = f'Проверка {element.type_of} "{element.name}"'
        with allure.step(step):
            element.check_visible()
            element.check_have_text(text)
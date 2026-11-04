from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger('BaseComponent')

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Проверка соответствует ли текущий URL шаблону {expected_url.pattern}'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)

    @staticmethod
    def check_element(element: BaseElement):
        step = f'Проверка {element.type_of} "{element.name}"'
        with allure.step(step):
            element.check_visible()
            element.check_have_text(element.name)





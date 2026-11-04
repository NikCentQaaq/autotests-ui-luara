

import allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger('INPUT')

class Input(BaseElement):

    # def get_locator(self, nth: int=0) -> Locator:
    #     return super().get_locator_test_id(nth).locator('input')


    def fill(self, value: str | int, nth: int=0):
        step = f'Заполняем {self.type_of} "{self.name}" значением {value}'

        with allure.step(step):
            locator = self.get_locator_test_id(nth)
            logger.info(step)

            locator.fill(value)


    def check_have_value(self, value: str | int, nth: int=0):
        step = f'Проверка, что {self.type_of} "{self.name}" имеет значение {value}'

        with allure.step(step):
            locator = self.get_locator_test_id(nth)
            logger.info(step)

            expect(locator).to_have_value(value)
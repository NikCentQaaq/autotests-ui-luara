import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger('BUTTON')


class Button(BaseElement):

    def check_enabled(self, nth: int=0):
        step = f'Проверка, что {self.type_of} "{self.name}" активен'

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            expect(locator).to_be_enabled()


    def check_disabled(self, nth: int=0):
        step = f'Проверка, что {self.type_of} "{self.name}" неактивен'

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            expect(locator).to_be_disabled()




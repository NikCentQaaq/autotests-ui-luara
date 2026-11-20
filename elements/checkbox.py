import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger('CHECKBOX')

class Checkbox(BaseElement):


    def check(self, nth: int = 0):
        step = f'Выбрать {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            locator.check()


    def uncheck(self, nth: int = 0):
        step = f'Снять выбор с {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            locator.uncheck()



    def check_checked(self, nth: int = 0):
        step = f'Проверка, что {self.type_of} "{self.name}" выбран'

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            expect(locator).to_be_checked()



    def check_not_checked(self, nth: int = 0):
        step = f'Проверка, что {self.type_of} "{self.name}" не выбран'

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            expect(locator).not_to_be_checked()


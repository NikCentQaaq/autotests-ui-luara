import allure
from playwright.sync_api import Page, Locator, expect

from tools.logger import get_logger

logger = get_logger('BASE_ELEMENT')


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self):
        return self.__class__.__name__


    def get_locator_test_id(self, nth: int=0) -> Locator:

        step = f'Получение локатора "data-test-id"="{self.locator}" с индексом "{nth}"'

        with allure.step(step):
            logger.info(step)

            return self.page.get_by_test_id(self.locator).nth(nth)




    def click(self, nth: int=0):

        step = f'Клик {self.type_of} "{self.name}"'

        with allure.step(step):

            locator = self.get_locator_test_id(nth)
            logger.info(step)

            locator.click()


    def check_visible(self, nth: int=0):

        step = f'Проверка, что {self.type_of} "{self.name}" виден'

        with allure.step(step):

             locator = self.get_locator_test_id(nth)
             logger.info(step)

             expect(locator).to_be_visible()


    def check_have_text(self, text: str, nth: int=0):

        step = f'Проверка, что {self.type_of} "{self.name}" имеет текст "{text}"'

        with allure.step(step):

            locator = self.get_locator_test_id(nth)
            logger.info(step)

            expect(locator).to_have_text(text)



    def check_contain_text(self, text: str, nth: int=0):

        step = f'Проверка, что {self.type_of} "{self.name}" содержит текст "{text}"'

        with allure.step(step):
            locator = self.get_locator_test_id(nth)
            logger.info(step)

            expect(locator).to_be_contain(text)






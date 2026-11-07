import allure

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger('SELECT')

class Select(BaseElement):


    def select_by_value(self, value: str, nth: int = 0):
        step = f'Выбор значения по value "{value}" в {self.type_of} "{self.name}" '

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            locator.select_option(value=value)



    def select_by_label(self, label: str, nth: int = 0):
        step = f'Выбор значения  по тексту "{label}" в {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth)
            logger.info(step)

            locator.select_option(label=label)




    def get_selected_value(self) -> str:
        step = 'Получение выбранного значения'

        with allure.step(step):
            logger.info(step)
            return self.locator.input_value()



    def check_selected_value(self, expected_value: str):
        step = f'Проверка, что в {self.type_of} "{self.name}" выбрано значение "{expected_value}"'

        with allure.step(step):
            logger.info(step)

            actual_value = self.get_selected_value()

            assert actual_value == expected_value, f'Ожидалось выбранное значение "{expected_value}", выбрано "{actual_value}"'


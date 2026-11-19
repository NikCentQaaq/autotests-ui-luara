import allure

from elements.button import Button
from tools.logger import get_logger

logger = get_logger('SLIDER')

class Slider(Button):

    def move(self, offset: int, nth: int = 0):
        """
        Перемещает элемент по горизонтали.
        """

        step = f'Перемещение {self.type_of} "{self.name}" на {offset}px'

        with allure.step(step):
            locator = self.get_locator(nth)

            logger.info(step)

            box = locator.bounding_box()

            if box is None:
                raise AssertionError(f'Не удалось получить координаты элемента "{self.name}"' )

            x = box["x"] + box["width"] / 2
            y = box["y"] + box["height"] / 2

            page = locator.page

            page.mouse.move(x, y)
            page.mouse.down()
            page.mouse.move(x + offset, y)
            page.mouse.up()
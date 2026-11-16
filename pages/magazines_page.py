import allure
from playwright.sync_api import Page

from components.headers.header_component import HeaderComponent
from elements.container import Container
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.routes import Rout


class MagazinesPage(BasePage):

    ROUTE = Rout.MAGAZINES

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)

        self.title = Text(page.get_by_role('heading', name='Фирменные салоны и магазины LUARA'), 'Фирменные салоны и магазины LUARA')

        self.city = Container(page.locator('details.shops-city'), 'Города')

    @allure.step("Проверка отображения всех городов")
    def check_cities(self):
        count = self.city.get_locator().count()

        for i in range(count):
            self.city.check_visible(nth=i)

    @allure.step("Проверка элементов страницы Магазинов")
    def check_elements(self):
        self.header.check_elements()
        self.check_element_text_by_name(self.title)
        self.check_cities()

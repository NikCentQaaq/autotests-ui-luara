import allure
from playwright.sync_api import Page

from components.headers.header_component import HeaderComponent
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from tools.enums.routes import Rout


class AktsiiPage(BasePage):

    ROUTE = Rout.AKTSII

    def __init__(self, page: Page):
        super().__init__(page)

        self.header = HeaderComponent(page)

        self.title = Text(page.get_by_role("heading", name='Акции'), 'Акции')
        self.podarok_za_otziv = Link(page.get_by_alt_text('Подарок за отзыв'), 'Подарок за отзыв')
        self.vam_podarok = Link(page.get_by_alt_text('Вам подарок*'), 'Вам подарок*')
        self.club = Link(page.get_by_alt_text('Клуб привилегий LUARA'), 'Клуб привилегий LUARA')
        self.dostavka = Link(page.get_by_alt_text('Доставка бесплатно'), 'Доставка бесплатно')
        self.chistka = Link(page.get_by_alt_text('Чистка украшений'), 'Чистка украшений')



    @allure.step("Проверка элементов страницы акций")
    def check_elements(self):

        self.check_element_text_by_name(self.title)
        self.podarok_za_otziv.check_visible()
        self.vam_podarok.check_visible()
        self.club.check_visible()
        self.dostavka.check_visible()
        self.chistka.check_visible()




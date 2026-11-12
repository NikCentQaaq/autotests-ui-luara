from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.concern_catalog.concern_card_component import CardConcernComponent
from components.concern_catalog.concern_nav_component import NavConcernComponent
from elements.text import Text
import allure

from tools.enums.category import Category


class ConcernCatalogComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator("section.concern")

        self.text_catalog = Text(self.container.get_by_text('Каталог'), 'Каталог')
        self.title_catalog = Text(self.container.get_by_text('Украшения для особых моментов'), 'Заголовок каталога')
        self.lead_catalog = Text(self.container.get_by_text('Выберите категорию и найдите своё идеальное украшение'), 'Описание каталога')

        self.cards = self.container.locator("a.concern-card")  # 7 карточек
        self.nav = NavConcernComponent(page)



    @allure.step('Проверка видимости 5 карт')
    def check_visible_5_cards(self):
        expect(self.container).to_be_visible()
        expect(self.cards).to_have_count(7)
        for i in range(5):  # отображается 4 элемента
            CardConcernComponent(self.page, self.cards.nth(i)).check_elements()

    @allure.step('Проверка элементов блока Каталога')
    def check_elements(self):

        self.check_element_text_by_name(self.text_catalog)

        self.check_element(self.title_catalog, 'Украшения для особых моментов')
        self.check_element(self.lead_catalog, 'Выберите категорию и найдите своё идеальное украшение')
        self.nav.check_elements()

        self.check_visible_5_cards()



    def open_card_by_category(self, category_name: Category):

        count = self.cards.count()
        for i in range(count):
            card = CardConcernComponent(self.page, self.cards.nth(i))

            if card.name.get_text() == category_name:
                card.click()
                return










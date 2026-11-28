from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.concern_catalog.concern_card_component import CardConcernComponent
from components.concern_catalog.concern_nav_component import NavConcernComponent
from elements.container import Container
from elements.text import Text
import allure

from tools.enums.category import Category


class ConcernCatalogComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = Container(page.locator("section.concern"), 'Блок "Каталог категорий"')

        self.text_catalog = Text(page.locator('section.concern').get_by_text('Каталог'), 'Каталог')
        self.title_catalog = Text(page.get_by_text('Украшения для особых моментов'), 'Заголовок каталога')
        self.lead_catalog = Text(page.get_by_text('Выберите категорию и найдите своё идеальное украшение'), 'Описание каталога')

        self.cards = page.locator("a.concern-card")  # 7 карточек
        self.nav = NavConcernComponent(page)



    @allure.step('Проверка видимости 5 карт')
    def check_visible_5_cards(self):
        self.container.check_visible()
        expect(self.cards).to_have_count(7)

        for i in range(self.cards.count()):
            card = self.cards.nth(i)

            print(f"\n========== КАРТОЧКА {i + 1} ==========")
            print("Текст:", card.inner_text())
            print("HTML:", card.evaluate("(el) => el.outerHTML"))
            print(
                "Количество элементов count:",
                card.locator("span.concern-card_count").count()
            )



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










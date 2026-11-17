import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.base_element import BaseElement
from elements.container import Container
from elements.link import Link



class TopHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = Container(page.locator(".page-wrap"), 'Top Header')


        self.phone = Link(page.get_by_role("link", name="8 (800) 333-81-17"),"Телефон")
        self.promo = Link(page.get_by_role('link', name='Акции'), 'Акции')
        self.delivery = Link(page.get_by_role('link', name='Доставка и оплата'), 'Доставка и оплата')
        self.shops = Link(page.get_by_role('link', name='Магазины'), 'Магазины')
        self.certificate = Link(page.get_by_role('link', name='Сертификат'), 'Сертификат')
        self.conditions = Link(page.get_by_role('link', name='Условия покупки'), 'Условия покупки')
        self.contacts = Link(page.get_by_role('link', name='Контакты'), 'Контакты')
        self.vacancies = Link(page.get_by_role('link', name='Вакансии'), 'Вакансии')


    @allure.step('Проверка элементов Top Header')
    def check_elements(self):

        self.phone.check_visible()
        self.phone.check_have_text('8 (800) 333-81-17')

        self.check_element_text_by_name(self.promo)
        self.check_element_text_by_name(self.delivery)
        self.check_element_text_by_name(self.shops)
        self.check_element_text_by_name(self.certificate)
        self.check_element_text_by_name(self.conditions)
        self.check_element_text_by_name(self.contacts)
        self.check_element_text_by_name(self.vacancies)

    @allure.step('Нажатие на "Акции"')
    def click_promo(self):
        self.promo.click()

    @allure.step('Нажатие на "Магазины"')
    def click_shops(self):
        self.shops.click()









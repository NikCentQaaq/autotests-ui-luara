import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.base_element import BaseElement
from elements.link import Link



class TopHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.container = page.locator(".page-wrap")

        self.phone = Link(self.container.get_by_role("link", name="8 (800) 333-81-17"),"Телефон")
        self.promo = Link(self.container.get_by_role('link', name='Акции'), 'Акции')
        self.delivery = Link(self.container.page.get_by_role('link', name='Доставка и оплата'), name='Доставка и оплата')
        self.shops = Link(self.container.get_by_role('link', name='Магазины'), name='Магазины')
        self.certificate = Link(self.container.get_by_role('link', name='Сертификат'), name='Сертификат')
        self.conditions = Link(self.container.get_by_role('link', name='Условия покупки'), name='Условия покупки')
        self.contacts = Link(self.container.get_by_role('link', name='Контакты'), name='Контакты')
        self.vacancies = Link(self.container.get_by_role('link', name='Вакансии'), name='Вакансии')


    @allure.step('Проверка элементов Top Header')
    def check_elements(self):

        self.phone.check_visible()
        self.phone.check_have_text('8 (800) 333-81-17')

        self.check_element(self.promo)
        self.check_element(self.delivery)
        self.check_element(self.shops)
        self.check_element(self.certificate)
        self.check_element(self.conditions)
        self.check_element(self.contacts)
        self.check_element(self.vacancies)






import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class LogoutModalComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.modal = page.locator(".modal-size_box").filter(has=page.locator("#lk_logout_title"))

        self.title = Text(page.locator('#lk_logout_title'),'Заголовок')
        self.description = Text(page.get_by_text('Заказы, бонусы и данные профиля останутся в аккаунте. Чтобы вернуться, войдите снова.'), 'Описание')

        self.logout_button = Button(self.modal.get_by_role('button', name='Выйти'), 'Выйти')
        self.stay_button = Button(page.get_by_role('button', name='Остаться'), 'Остаться')
        self.close_button = Button(page.get_by_role('button', name='Закрыть'), 'Закрыть')




    @allure.step('Проверка элементов модального окна Logout')
    def check_elements(self):
        self.title.check_visible()
        self.title.check_have_text('Выйти из личного кабинета?')
        self.description.check_visible()
        self.description.check_have_text('Заказы, бонусы и данные профиля останутся в аккаунте. Чтобы вернуться, войдите снова.')

        self.logout_button.check_visible()
        self.stay_button.check_visible()

    @allure.step('Нажатие кнопки Выйти')
    def click_logout_button(self):
        self.logout_button.click()

    @allure.step('Нажатие кнопки Остаться')
    def click_stay_button(self):
        self.stay_button.click()



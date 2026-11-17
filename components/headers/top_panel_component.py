from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.link import Link


class TopPanelComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.img_panel = Link(page.get_by_role("link",name="Клуб привилегий LUARA"), 'Панель "Клуб привилегий"')
        self.close_button = Button(page.locator('div.close'), 'Закрыть панель')


    def check_elements(self):
        self.img_panel.check_visible()
        self.close_button.check_visible()


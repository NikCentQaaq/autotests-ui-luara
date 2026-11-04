from components.base_component import BaseComponent
from elements.button import Button


class HelpMenuComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.trigger = Button(page,"header-help-menu","Помощь")

        # self.faq = Link(...)
        # self.booking = Link(...)
        # self.gift = Link(...)
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.filter.search_filter import SearchFilterComponent


class FilterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.search = SearchFilterComponent(page)


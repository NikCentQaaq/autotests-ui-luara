import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage


@pytest.fixture
def main_page(page: Page) -> MainPage:
    return MainPage(page=page)

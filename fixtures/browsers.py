import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page
from config import settings
from tools.playwright.playwright_page import initialize_playwright_page


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:

    yield from initialize_playwright_page(
        playwright=playwright,
        test_name=request.node.name,
        browser_type=request.param
    )


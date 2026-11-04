from playwright.sync_api import Page


def test_url(page: Page):
    page.goto("https://www.sputnik8.com/")
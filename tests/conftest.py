from playwright.sync_api import Page

import pytest


@pytest.fixture(autouse=True)
def accept_cookies(page: Page):
    page.goto("https://www.avast.com/en-us/")
    page.locator("#onetrust-accept-btn-handler").click()
    yield

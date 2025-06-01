import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def accept_cookies(page: Page):
    page.goto("https://www.avast.com/en-us/")
    page.locator("#onetrust-accept-btn-handler").click()
    yield


@pytest.fixture()
def android_page(playwright, request):
    samsung = playwright.devices["Galaxy S9+"]
    browser = playwright.chromium.launch()
    context = browser.new_context(**samsung)
    page = context.new_page()
    page.goto("https://www.avast.com/en-us/")
    page.locator("#onetrust-accept-btn-handler")
    yield page
    context.close()
    browser.close()

#comment
@pytest.fixture()
def ios_page(playwright):
    iphone = playwright.devices["iPhone 12"]
    browser = playwright.webkit.launch()
    context = browser.new_context(**iphone)
    page = context.new_page()
    page.goto("https://www.avast.com/en-us/")
    page.locator("#onetrust-accept-btn-handler")
    yield page
    context.close()
    browser.close()

from playwright.sync_api import Page, expect

import pytest
import re


@pytest.fixture(scope="function")
def go_to_store(page: Page):
    page.get_by_role("menuitem", name="Store").click()
    yield


class TestStorePage:
    @pytest.fixture(autouse=True)
    def setup_store(self, go_to_store):
        pass

    @pytest.mark.skip(reason="not need to test this now")
    def test_url_is_right(self, page: Page):
        expect(page).to_have_url(re.compile(r"/store"))

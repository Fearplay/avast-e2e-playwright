import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function")
def go_to_store(page: Page):
    page.get_by_role("menuitem", name="Store").click()
    yield


class TestStorePage:
    @pytest.fixture(autouse=True)
    def setup_store(self, go_to_store):
        pass

    @pytest.mark.desktoptest
    def test_url_is_right(self, page: Page):
        """Test that the 'store page' has 'store' url"""
        expect(page).to_have_url(re.compile(r"/store"))

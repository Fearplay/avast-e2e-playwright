import re

import pytest
from playwright.sync_api import Page, expect


#    @pytest.mark.skip(reason="not need to test this now") - use this for skip tests

class TestHomePage:
    @pytest.mark.desktoptest
    def test_cookies_are_not_visible(self, page: Page):
        """Test that the cookies are hidden."""
        expect(page.locator("#onetrust-banner-sdk")).to_be_hidden()

    @pytest.mark.desktoptest
    def test_avast_icon_alt(self, page: Page):
        """Test that the alt text with 'Avast' text is visible."""
        expect(page.get_by_alt_text("Avast")).to_be_visible()

    @pytest.mark.desktoptest
    def test_check_default_page_is_for_homepage(self, page: Page):
        """Test that the 'for home' button is marked as active."""
        expect(page.get_by_role("menuitem", name="For home")).to_have_attribute("aria-current", "true")

    @pytest.mark.desktoptest
    def test_check_button_home_redirects(self, page: Page):
        """Test that the 'for home' button works."""
        page.get_by_role("menuitem", name="For home").click()
        expect(page).to_have_url(re.compile(r"/index"))

    @pytest.mark.desktoptest
    def test_check_button_business_redirects(self, page: Page):
        """Test that the 'for business' button works."""
        page.get_by_role("menuitem", name="For business").click()
        expect(page).to_have_url(re.compile(r"/business"))

    @pytest.mark.desktoptest
    def test_check_button_partners_redirects(self, page: Page):
        """Test that the 'for partners' button works."""
        page.get_by_role("menuitem", name="For partners").click()
        expect(page).to_have_url(re.compile(r"/partners"))

    @pytest.mark.desktoptest
    def test_check_button_store_redirects(self, page: Page):
        """Test that the 'store' button works."""
        page.get_by_role("menuitem", name="Store").click()
        expect(page).to_have_url(re.compile(r"/store"))

    @pytest.mark.desktoptest
    def test_check_button_all_products_redirects(self, page: Page):
        """Test that the 'all pc products' button works."""
        page.get_by_text("All PC products").click()
        expect(page).to_have_url(re.compile(r"/store"))

    @pytest.mark.desktoptest
    def test_check_button_get_premium_redirects(self, page: Page):
        """Test that the 'get premium' button works."""
        page.locator(".btn.full.size-lg.theme-gold.ms-lg-24").click()
        expect(page).to_have_url(re.compile(r"/store"))

    @pytest.mark.desktoptest
    def test_check_button_compare_products_redirects(self, page: Page):
        """Test that the 'compare products' button works."""
        page.get_by_text("Compare products").click()
        expect(page).to_have_url(re.compile(r"/compare-antivirus"))

    @pytest.mark.desktoptest
    def test_free_download_triggers_download(self, page: Page):
        """Test that the download button works."""
        with page.expect_download():
            page.locator(".btn.full.size-lg.theme-blue.btn-icon-left.bi-download-link.js-pc.mb-16.mb-lg-0").click()

from playwright.sync_api import Page, expect

import pytest
import re


class TestHomePage:
    @pytest.mark.skip(reason="not need to test this now")
    def test_cookies_are_not_visible(self, page: Page):
        expect(page.locator("#onetrust-banner-sdk")).to_be_hidden()

    @pytest.mark.skip(reason="not need to test this now")
    def test_avast_icon_alt(self, page: Page):
        expect(page.get_by_alt_text("Avast")).to_be_visible()

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_default_page_is_for_homepage(self, page: Page):
        expect(page.get_by_role("menuitem", name="For home")).to_have_attribute("aria-current", "true")

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_button_home_redirects(self, page: Page):
        page.get_by_role("menuitem", name="For home").click()
        expect(page).to_have_url(re.compile(r"/index"))

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_button_business_redirects(self, page: Page):
        page.get_by_role("menuitem", name="For business").click()
        expect(page).to_have_url(re.compile(r"/business"))

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_button_partners_redirects(self, page: Page):
        page.get_by_role("menuitem", name="For partners").click()
        expect(page).to_have_url(re.compile(r"/partners"))

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_button_store_redirects(self, page: Page):
        page.get_by_role("menuitem", name="Store").click()
        expect(page).to_have_url(re.compile(r"/store"))

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_button_all_products_redirects(self, page: Page):
        page.get_by_text("All PC products").click()
        expect(page).to_have_url(re.compile(r"/store"))

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_button_get_premium_redirects(self, page: Page):
        page.locator(".btn.full.size-lg.theme-gold.ms-lg-24").click()
        expect(page).to_have_url(re.compile(r"/store"))

    @pytest.mark.skip(reason="not need to test this now")
    def test_check_button_compare_products_redirects(self, page: Page):
        page.get_by_text("compare-antivirus").click()
        expect(page).to_have_url(re.compile(r"/compare-antivirus"))

    @pytest.mark.skip(reason="not need to test this now")
    def test_free_download_triggers_download(self, page: Page):
        with page.expect_download():
            page.locator(".btn.full.size-lg.theme-blue.btn-icon-left.bi-download-link.js-pc.mb-16.mb-lg-0").click()

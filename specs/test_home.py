from seleniumbase import BaseCase
from pages.home_page import HomePage
import pytest


class TestHomePage(BaseCase):

    def setUp(self, masterqa_mode=False):
        super().setUp(masterqa_mode)  # call the setyp of the parent class if needed
        self.homepage = HomePage(self)
        self.homepage.open()

        print("Login")

    def tearDown(self):
        print("Log Out")
        super().tearDown()

    @pytest.mark.smoke
    def test_verify_page_title_and_url(self):

        self.assert_url_contains("sdetunicorns")

        self.assert_title_contains("SDET Unicorns")

        print("TEST")

    def test_search_flow(self):
        self.homepage.search_for_item("Lenovo")
        self.assert_text_visible("Showing Results for Lenovo")

    def test_nav_links(self):

        self.assert_text("Products", ".main-menu li:nth-child(2)")

        expected_nav_text = ["Home", "Products", "About Us", "Contact", "Upload"]

        self.homepage.verify_nav_links(expected_nav_text)

    def test_new_tab(self):

        self.click('a[href="https://sdetunicorns.com"]')
        self.switch_to_newest_tab()
        self.assert_title_contains("Master")
        self.switch_to_default_tab()
        self.assert_title_contains("Practice")

from seleniumbase import BaseCase
from pages.home_page import HomePage


class TestHomePage(BaseCase):

    def test_verify_page_title_and_url(self):
        homepage = HomePage(self)
        homepage.open()
        self.assert_url_contains("sdetunicorns")

        self.assert_title_contains("SDET Unicorns")

    def test_search_flow(self):
        homepage = HomePage(self)
        homepage.open()
        homepage.search_for_item("Lenovo")
        self.assert_text_visible("Showing Results for Lenovo")

    def test_nav_links(self):
        homepage = HomePage(self)
        homepage.open()

        self.assert_text("Products", ".main-menu li:nth-child(2)")

        expected_nav_text = ["Home", "Products", "About Us", "Contact", "Upload"]

        homepage.verify_nav_links(expected_nav_text)

    def test_new_tab(self):
        homepage = HomePage(self)
        homepage.open()

        self.click('a[href="https://sdetunicorns.com"]')
        self.switch_to_newest_tab()
        self.assert_title_contains("Master")
        self.switch_to_default_tab()
        self.assert_title_contains("Practice")

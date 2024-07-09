from seleniumbase import BaseCase


class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.assert_url_contains("sdetunicorns")

        self.assert_title_contains("SDET Unicorns")

    def test_search_flow(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.click('button[class="search-active"]')

        self.type('input[placeholder="Search"]', 'Lenovo\n')

        self.assert_text('Showing Results for Lenovo', 'h3[class="text-center py-3"]')
from seleniumbase import BaseCase

class TestContactPage(BaseCase):
    def test_verify_page_title_and_url(self):
        self.open("https://practice-react.sdetunicorns.com/contact")

        self.click('button[type="submit"]')

        self.assert_exact_text("Name is required", 'p[class="error-name"]')
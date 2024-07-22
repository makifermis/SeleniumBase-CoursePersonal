from seleniumbase import BaseCase

class TestHomePage(BaseCase):
    def test_verify_aboutUsPage_url(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.click('.footer-list a[href="/about"]')

        self.assert_url_contains("about")

        self.assert_title_contains("About")

    def test_nav_categories(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.click('.main-menu a[href="/shop-grid-standard"]')        

        expected_categories = ['All Categories','Laptop', 'Electronics', 'Keyboard']

        for i, text in enumerate(expected_categories, start=1):
            print(i,text)
            self.assert_text(text, f"[class='sidebar-widget-list mt-30'] li:nth-of-type({i}) button")
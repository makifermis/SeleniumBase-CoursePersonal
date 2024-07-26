from seleniumbase import BaseCase

class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.assert_url_contains("sdetunicorns")

        self.assert_title_contains("SDET Unicorns")

    def test_search_flow(self):
        self.open("https://practice-react.sdetunicorns.com/")
     
        self.click('//button[@class="search-active"]')
        
        self.type('//input[@placeholder="Search"]', 'Lenovo\n')
    
        self.assert_text('Showing Results for Lenovo', '//h3[@class="text-center py-3"]')
        self.wait(5)

    def test_nav_links(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.assert_text('Products','.main-menu li:nth-child(2)')

        expected_nav_text = ['Home', 'Products', 'About Us', 'Contact', 'Upload']

        for i, text in enumerate(expected_nav_text, start=1):
            print(i, text)
            self.assert_text(text, f'.main-menu li:nth-child({i})')

    def test_new_tab(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.click('a[href="https://sdetunicorns.com"]')
        self.switch_to_newest_tab()
        self.assert_title_contains('Master')
        self.switch_to_default_tab()
        self.assert_title_contains('Practice')

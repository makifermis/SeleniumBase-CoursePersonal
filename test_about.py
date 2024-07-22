from seleniumbase import BaseCase

class TestAboutPage(BaseCase):
    def test_assert_equal(self):
        self.open("https://practice-react.sdetunicorns.com/")

        self.click('.footer-list a[href="/about"]')

        text = self.get_text('div h5')

        self.assert_equal(text,"Who Are We")
    
    def test_assert_true(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        is_element_visible = self.is_element_visible('.breadcrumb-content')

        self.assert_true(is_element_visible)

    def test_assert_element_visible(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_element_visible('.banner-area')
    
    def test_assert_element_present(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        self.assert_element_present('#hidden-span')

    def test_assert_in(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        welcome_text = self.get_text('.welcome-content>h1')

        print(welcome_text)
       
        self.assert_in('Welcome', welcome_text)

    def test_assert_attribute(self):
        self.open("https://practice-react.sdetunicorns.com/about")
       
        self.assert_attribute('.breadcrumb-content a', 'aria-current', 'page')

    def test_assert_notVisible(self):
        self.open("https://practice-react.sdetunicorns.com/about")
       
        self.assert_element_not_visible('#hidden-span')

    def test_assert_notEqual(self):
        self.open("https://practice-react.sdetunicorns.com/about")

        order_limit = self.get_text('p span')

        order_limit_without_sign = order_limit[1]

        order_limit_int = int(order_limit_without_sign)
       
        self.assert_not_equal(order_limit_int, 0, 'Order limit can not be zero')    
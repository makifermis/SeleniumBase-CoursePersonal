from seleniumbase import BaseCase
import os.path

class TestUploadPage(BaseCase):

    def test_upload_single_file(self):
        self.open('https://practice-react.sdetunicorns.com/upload')

        file_path = os.path.abspath("data/seleniumbase_logo.png")
        target_element = '.single [type="file"]'

        print(file_path)

        #self.drag_and_drop_file(file_path, target_element)

        self.choose_file(target_element, file_path)

        self.assert_element('.preview img')

        self.click('button.btn-primary')

        self.assert_text('Image uploaded successfully', '[class="react-toast-notifications__toast__content css-1ad3zal"]')

    def test_upload_multiple_file(self):
        self.open('https://practice-react.sdetunicorns.com/upload')

        file_paths = [os.path.abspath("data/seleniumbase_logo.png"),os.path.abspath("data/seleniumbase_logo2.png")]
        target_element = '.multiple [type="file"]'

        #print(file_path)

        files_to_upload = "\n".join(file_paths)

        #self.drag_and_drop_file(file_path, target_element)

        self.choose_file(target_element, files_to_upload)

        self.assert_element('.preview img')

        self.click('button.btn-primary')

        self.assert_text('Images uploaded successfully', '[class="react-toast-notifications__toast__content css-1ad3zal"]')
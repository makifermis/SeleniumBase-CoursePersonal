from seleniumbase import BaseCase
import os.path
from pages.upload_page import UploadPage


class TestUploadPage(BaseCase):

    def test_upload_1_single_file(self):
        uploadpage = UploadPage(self)
        uploadpage.open()

        file_path = os.path.abspath("data/seleniumbase_logo.png")

        uploadpage.upload_single_file(file_path)

        self.assert_text(
            "Image uploaded successfully",
            '[class="react-toast-notifications__toast__content css-1ad3zal"]',
        )

    def test_upload_2_multiple_file(self):
        uploadpage = UploadPage(self)
        uploadpage.open()

        file_paths = [
            os.path.abspath("data/seleniumbase_logo.png"),
            os.path.abspath("data/seleniumbase_logo2.png"),
        ]

        uploadpage.upload_multiple_files(file_paths)

        self.assert_text(
            "Images uploaded successfully",
            '[class="react-toast-notifications__toast__content css-1ad3zal"]',
        )

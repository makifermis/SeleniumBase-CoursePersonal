from seleniumbase import BaseCase
from pages.upload_page import UploadPage
from utils.helpers import get_image_path
import pytest


class TestUploadPage(BaseCase):

    @pytest.mark.smoke
    def test_upload_1_single_file(self):
        uploadpage = UploadPage(self)
        uploadpage.open()

        file_path = get_image_path("seleniumbase_logo.png")

        uploadpage.upload_single_file(file_path)

        self.assert_text(
            "Image uploaded successfully",
            '[class="react-toast-notifications__toast__content css-1ad3zal"]',
        )

    def test_upload_2_multiple_file(self):
        uploadpage = UploadPage(self)
        uploadpage.open()

        file_paths = [
            get_image_path("seleniumbase_logo.png"),
            get_image_path("seleniumbase_logo2.png"),
        ]

        uploadpage.upload_multiple_files(file_paths)

        self.assert_text(
            "Images uploaded successfully",
            '[class="react-toast-notifications__toast__content css-1ad3zal"]',
        )

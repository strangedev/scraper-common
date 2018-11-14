import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from scraper_common.webdriver import WebDriver


class TestWebdriver(unittest.TestCase):
    def test_webdriver_is_configured(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.close()

    def test_create_new_webdriver(self):
        self.assertIsNotNone(WebDriver().d)

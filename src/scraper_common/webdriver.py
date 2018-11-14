from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from scraper_common.singleton import SingletonMeta


class WebDriver(metaclass=SingletonMeta):
    def __init__(self, headless: bool=True):
        self._driver = WebDriver.newWebDriver(headless=headless)

    def __del__(self):
        self._driver.close()

    @property
    def d(self) -> webdriver.Chrome:
        return self._driver

    @staticmethod
    def newWebDriver(headless: bool=True) -> webdriver.Chrome:
        """Creates a new WebDriver instance.

        Args:
            headless: Whether the WebDriver should use a headless browser.

        Returns:
            A new :class:`selenium.WebDriver` instance.
        """
        options = Options()
        options.headless = headless
        driver = webdriver.Chrome(options=options)
        return driver

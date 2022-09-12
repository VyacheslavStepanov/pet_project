from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """ Base class for all Page Classes """

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def is_current_page(self):
        return self._base_url in self._driver.current_url

    def open(self):
        self._driver.get(self._base_url)

from selenium.webdriver.common.by import By

from ui.base_page import BasePage


class GooglePage(BasePage):
    _base_url = "https://www.google.com"

    @property
    def search_input(self):
        return self._driver.find_element(By.XPATH, "//input[@name='q']")

    @property
    def search_results(self):
        return self._driver.find_elements(By.XPATH, "//div[@id='search']//a")

    def get_search_results_by_text(self, text):
        return self._driver.find_elements(
            By.XPATH, f"//div[@id='search']//a[contains(@href, '{text}')]"
        )

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from ui.google_page import GooglePage
from ui.time24_page import Time24Page


@pytest.fixture(scope="session")
def driver() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver

    driver.close()


@pytest.fixture(scope="function")
def google_page(driver):
    return GooglePage(driver)


@pytest.fixture(scope="function")
def time24_page(driver):
    return Time24Page(driver)

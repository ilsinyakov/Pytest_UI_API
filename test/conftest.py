from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser

    browser.quit()
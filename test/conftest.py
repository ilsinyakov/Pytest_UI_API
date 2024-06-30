import allure
from selenium import webdriver
import pytest
# from time import sleep


@pytest.fixture
def browser():
    with allure.step('Open browser'):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step('Close browser'):
        browser.quit()

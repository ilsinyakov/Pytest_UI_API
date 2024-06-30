import allure
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = 'https://id.atlassian.com/login?application=trello'
        self.__driver = driver

    @allure.step('Go to auth page')
    def go(self):
        self.__driver.get(self.__url)

    @allure.step('Log in')
    def login_as(self, email: str, password: str) -> None:
        user_name_field = self.__driver.find_element(By.ID, 'username')
        user_name_field.send_keys(email)

        submit_button = self.__driver.find_element(By.ID, 'login-submit')
        submit_button.click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              'svg[role="presentation"]'))
            )

        password_field = self.__driver.find_element(By.ID, 'password')
        password_field.send_keys(password)

        login_button = self.__driver.find_element(By.ID, 'login-submit')
        login_button.click()

        sleep(5)
        trello_link = self.__driver.\
            find_element(By.CSS_SELECTOR, '[href^="https://trello.com"]')
        trello_link.click()

    @allure.step('Get current url')
    def get_current_url(self) -> str:
        return self.__driver.current_url

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = 'https://id.atlassian.com/login?application=trello'
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str) -> None:
        user_name_field = self.__driver.find_element(By.ID, 'username')
        user_name_field.send_keys(email)

        submit_button = self.__driver.find_element(By.ID, 'login-submit')
        submit_button.click()

        password_field = self.__driver.find_element(By.ID, 'password')
        password_field.send_keys(password)

        login_button = self.__driver.find_element(By.ID, 'login-submit')
        login_button.click()

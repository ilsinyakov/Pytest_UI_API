from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def open_menu(self) -> None:
        menu_button = self.__driver.\
            find_element(By.CSS_SELECTOR,
                         '[data-testid="header-member-menu-button"]')
        menu_button.click()

    def get_account_info(self) -> list[str]:
        name_element = self.__driver.find_element(
            By.XPATH, '//*[@data-testid="account-menu"]'
                      '/div[1]/div/div[2]/div[1]'
                      )
        name = name_element.text

        email_element = self.__driver.find_element(
            By.XPATH, '//*[@data-testid="account-menu"]'
                      '/div[1]/div/div[2]/div[2]'
                      )
        email = email_element.text

        return [name, email]

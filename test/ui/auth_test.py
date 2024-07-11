# from time import sleep
import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def auth_test(browser, test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")
    username = test_data.get("username")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    with allure.step('Check log in URL'):
        assert auth_page.get_current_url().endswith('ilyasinyakov/boards')

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    with allure.step('Check user info'):
        assert info[0] == username and info[1] == email

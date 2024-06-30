from time import sleep
from pages.AuthPage import AuthPage


def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as('ilsinyakov@gmail.com', 'skyproskypro')

    assert auth_page.get_current_url().endswith('ilyasinyakov/boards')
    sleep(10)

# from time import sleep
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as('ilsinyakov@gmail.com', 'skyproskypro')

    assert auth_page.get_current_url().endswith('ilyasinyakov/boards')

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    assert info[0] == 'Ilya Sinyakov' and info[1] == 'ilsinyakov@gmail.com'    

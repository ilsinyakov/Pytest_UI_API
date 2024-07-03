import allure
from selenium import webdriver
import pytest
from api.BoardsApi import BoardsApi
# from time import sleep


base_url = 'https://trello.com/1'
token = ('eyJraWQiOiJzZXNzaW9uLXNlcnZpY2UvcHJvZC0xNTkyODU4Mzk0IiwiYWxnIjoiUlMy'
         'NTYifQ.eyJhc3NvY2lhdGlvbnMiOltdLCJzdWIiOiI3MTIwMjA6ZDYxNmI0NTgtNGEzY'
         'y00MDVhLThhMzAtNWNjYmYwYmEyNDVjIiwiZW1haWxEb21haW4iOiJnbWFpbC5jb20iL'
         'CJpbXBlcnNvbmF0aW9uIjpbXSwiY3JlYXRlZCI6MTcxOTc1MDE5MCwicmVmcmVzaFRpb'
         'WVvdXQiOjE3MTk5NDA3MDQsInZlcmlmaWVkIjp0cnVlLCJpc3MiOiJzZXNzaW9uLXNlc'
         'nZpY2UiLCJzZXNzaW9uSWQiOiI1MWY0YWNhNi1mN2Y3LTQ3MWUtYTU3OS04MzY1OThjM'
         'jlhMzAiLCJzdGVwVXBzIjpbXSwiYXVkIjoiYXRsYXNzaWFuIiwibmJmIjoxNzE5OTQwM'
         'TA0LCJleHAiOjE3MjI1MzIxMDQsImlhdCI6MTcxOTk0MDEwNCwiZW1haWwiOiJpbHNpb'
         'nlha292QGdtYWlsLmNvbSIsImp0aSI6IjUxZjRhY2E2LWY3ZjctNDcxZS1hNTc5LTgzN'
         'jU5OGMyOWEzMCJ9.zwTgEL1fQxI5_l8OijLTpwPAz9WKd1SKGz4EDb_gtJKTLYWPNtzJ'
         'PLlbMlkUfLskuoScGGCAaNRkajhEm16HwYBfZi_a-sc_PKveSB9yfRAhVtaWXYWUme8f'
         '_uF0C1CHXsezj3xW2i-GEGBfJs8B4MD6Tu-H49uAhBAi-O01EWf4sAUQZq2Lv-Z00CHr'
         'xCVOiK32WBGyqJ6smU396_SO8VS0ZVniQupXvA03bT1ayF6C2N4l29BRuidgOuEOdtyK'
         'd89uP50VjgA3DXhpSp2Zk_-1KFIkX3ivtRgS7IslknXlZBNvLtXD4-uhLYI0I09XMADT'
         '06Jjhu8zoHsvLWuorA')


@pytest.fixture
def browser():
    with allure.step('Open browser'):
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step('Close browser'):
        browser.quit()


@pytest.fixture
def board_api_client() -> BoardsApi:
    return BoardsApi(base_url, token)


@pytest.fixture
def board_api_client_no_auth() -> BoardsApi:
    return BoardsApi(base_url, '')


@pytest.fixture
def board_id_to_delete() -> str:
    api = BoardsApi(base_url, token)
    json = api.post_board('to_delete')
    return json["id"]


@pytest.fixture
def delete_board() -> dict:
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardsApi(base_url, token)
    api.delete_board(dictionary.get("board_id"))

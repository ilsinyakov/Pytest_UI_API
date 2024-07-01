from api.BoardsApi import BoardsApi


def test_get_boards():
    api = BoardsApi()
    boards_list = api.get_all_boards_by_org_id('6505743d43de02581a0f2a74')
    print(boards_list)

from api.BoardsApi import BoardsApi


def test_create_board(board_api_client: BoardsApi, delete_board: dict):
    json = board_api_client.post_board('test10')
    print('\n', json)
    print(json["name"])

    new_board_id = json["id"]

    delete_board["board_id"] = new_board_id


def test_delete_board(board_api_client: BoardsApi, board_id_to_delete: str):
    code = board_api_client.delete_board(board_id_to_delete)
    print('\n', code)

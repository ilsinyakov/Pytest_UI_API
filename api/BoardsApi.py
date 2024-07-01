import requests


class BoardsApi:
    base_url = 'https://api.trello.com/1'

    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        path = f'{self.base_url}/organizations/{org_id}/boards'
        print(path)
        resp = requests.get(path)

        return resp.json()

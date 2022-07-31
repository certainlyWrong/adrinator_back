
import os

from requests import request
# import sqlite3
from adrinator.api.Iadrinator_api import IAdrinatorServer


class Adrinator_GH_API_V1(IAdrinatorServer):
    """
    Version 1 of the API for adrinator project.
    """

    def __init__(self, pathTempDir: str, user: str) -> None:
        # self._conn.row_factory = sqlite3.Row
        self._pathFile = os.path.abspath(os.path.dirname(__file__))
        # self._conn = sqlite3.connect(f'{self._pathFile}/database_v1.db')
        self._GH_API = 'https://api.github.com'
        self._user = user

    def get_request(self) -> dict:
        return request(
            'GET',
            f'{self._GH_API}/users/{self._user}',
            headers={'Authorization': f'token {self._gh_token}'}
        ).json()

    def init(self) -> bool:
        self._gh_token = None

        """
        The try/except block is used to catch the exception raised when the
        token is not provided. The token is used to authenticate the user in
        the GitHub API. The production flag is used to determine if the server
        should run in production mode or not.
        """
        try:
            with open(
                    os.path.join(
                        os.path.dirname(__file__), 'token'), 'r') as f:

                print(os.path.join(os.path.dirname(__file__), 'token'))
                self._gh_token = f.read()
                return True

        except FileNotFoundError:
            self._gh_token = os.environ.get('GH_API')

            if self._gh_token is None:
                print('No token found. Please set GH_API environment.')
                return False
            return True

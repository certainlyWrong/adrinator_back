
import os

# import sqlite3
import json as json_lib
from requests import request
from adrinator.api.Iadrinator_api import IAdrinatorServer


class Adrinator_GH_API_V1(IAdrinatorServer):
    """
    Version 1 of the API for adrinator project.
    """

    def __init__(self, pathTempDir: str, user: str) -> None:
        # self._conn.row_factory = sqlite3.Row

        # path to the database for APIs of the Adrinator project
        self._pathFile = os.path.abspath(os.path.dirname(__file__))

        # self._conn = sqlite3.connect(f'{self._pathFile}/database_v1.db')

        # URL for the GitHub API
        self._GH_API = 'https://api.github.com'

        # User name of the user to get the data from the GitHub API.
        self._user = user

    def get_request(self, requests: list[str]) -> dict:

        match requests:
            case ['user', 'name']:
                return self._get_user_name()

            case ['user', 'repos']:
                return self._get_user_repos()

            case ['user', 'info']:
                return self._get_user_info()

            case ['user', 'orgs']:
                return self._get_user_orgs()

            case _:
                return {
                    'status': 'API not found'
                }

    def _get_user_name(self) -> dict:
        return {
            'status': 'ok',
            'name': self._user
        }

    def _get_user_repos(self) -> dict:
        """
        The method is used to get the list of repositories of the user.
        """
        url = f'{self._GH_API}/users/{self._user}/repos'
        response = request('GET', url, headers=self._headers)

        if response.status_code == 200:
            return {
                'status': 'ok',
                'repos': response.json()
            }
        else:
            return {
                'status': 'error',
                'message': response.json()['message']
            }

    def _get_user_info(self) -> dict:
        """
        The method is used to get the information of the user.
        """
        url = f'{self._GH_API}/users/{self._user}'
        response = request('GET', url, headers=self._headers)

        informations = self._get_information('github')

        response_json: dict = {}

        # Create a dictionary auxiliary to store the information of the user.
        response_json_aux = response.json()
        for i in informations:
            response_json[i] = response_json_aux[i]

        # delete for free memory.
        del response_json_aux, informations

        if response.status_code == 200:
            return {
                'status': 'ok',
                'user': response_json
            }
        else:
            return {
                'status': 'error',
                'message': response.json()['message']
            }

    def _get_user_orgs(self) -> dict:
        """
        The method is used to get the list of organizations of the user.
        """
        url = f'{self._GH_API}/users/{self._user}/orgs'
        response = request('GET', url, headers=self._headers)

        if response.status_code == 200:
            return {
                'status': 'ok',
                'orgs': response.json()
            }
        else:
            return {
                'status': 'error',
                'message': response.json()['message']
            }

    def _get_information(self, infor: str) -> list[str]:
        """
        The method is used to get the key information
        """

        with open(f'{self._pathFile}/get_informations.json', 'r') as f:
            return json_lib.decoder.JSONDecoder().decode(
                f.read()
            )[infor]['listOfGetInformations']

    def init(self) -> bool:
        self._headers = None

        # headers used to authenticate the user in the GitHub API
        self._gh_token = None
        validate: bool = False

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
                self._gh_token = f.read()
                validate = True

        except FileNotFoundError:
            self._gh_token = os.environ.get('GH_API')
            if self._gh_token is None:
                print('No token found. Please set GH_API environment.')
                validate = False
            validate = True

        if validate:
            self._headers = {'Authorization': f'token {self._gh_token}'}
            return True
        return validate

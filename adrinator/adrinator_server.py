
import os
import sqlite3
import logging
import requests as rq
from flask import Flask
from flask_cors import cross_origin

logging.getLogger('flask_cors').level = logging.DEBUG


class Server:
    """
    Class for the gerencial server of the Adrinator project.
    """
    _app = Flask(__name__)
    _path = os.path.abspath(os.path.dirname(__file__))
    _conn = sqlite3.connect(f'{_path}/database.db')
    _GH_API = 'https://api.github.com/'
    _conn.row_factory = sqlite3.Row
    _TOKEN = ''

    """
    Router for get github user information in API.
    """
    @_app.route('/github/user/<username>', methods=['GET'])
    @cross_origin()
    def get_github_user(username):
        """
        Get github user information.
        """
        result = rq.request(
            'GET',
            f'{Server._GH_API}users/{username}?token={Server._TOKEN}')
        print(result.headers)
        return result.json()

    @classmethod
    def run(cls, token: str, production: bool = False):
        cls._TOKEN = token

        port = int(os.environ.get("PORT", 8000))
        cls._app.run(host='0.0.0.0', port=port, debug=not production)

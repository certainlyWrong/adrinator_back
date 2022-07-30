
import os
import sqlite3
from flask import Flask

app = Flask(__name__)


class AdrinatorAppV1:
    """
    Version 1 of the API for adrinator project.
    """

    def __init__(self, token: str):
        self._path = os.path.abspath(os.path.dirname(__file__))
        self._conn = sqlite3.connect(f'{self._path}/database.db')
        self._GH_API = 'https://api.github.com/'
        self._conn.row_factory = sqlite3.Row
        self._TOKEN = token

    @app.route('/v1/json', methods=['GET'])
    def index(self):
        return {'title': 'Adrinator', 'content': self._GH_API}

    def run(self):
        port = int(os.environ.get("PORT", 8000))
        app.run(host='0.0.0.0', port=port)

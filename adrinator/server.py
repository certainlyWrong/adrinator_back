
import os
from flask import Flask
from adrinator.api.Iadrinator_api import IAdrinatorServer


class Server:
    """
    Class for the gerencial server version API of the Adrinator project.
    """
    _app = Flask(__name__)
    _api_v1: list[IAdrinatorServer] = []

    @classmethod
    def is_production(cls) -> bool:
        """
        The method is used to determine if the server
        should run in production mode or not.
        """
        return os.environ.get('PRODUCTION') == 'True'

    @classmethod
    def _init_APIs(cls) -> None:
        """
        The method is used to initialize the APIs.
        """
        for api in cls._api_v1:
            api.init()

    # Flask capitalized the first letter of the method name.
    @_app.route('/<path:path>')
    def _manager(path):
        """
        The method is used to greet the user.
        """
        return f'Hello {path}'

    @classmethod
    def run(cls, AdrinatorApps: list[IAdrinatorServer]) -> None:
        # Instance of the AdrinatorAppV1 class.
        cls._api_v1 = AdrinatorApps

        # Initialize the APIs.
        cls._init_APIs()

        # Get port from environment variable or choose the default one.
        port = int(os.environ.get("PORT", 8000))

        # Run the server.
        cls._app.run(host='0.0.0.0', port=port,
                     debug=not cls.is_production())

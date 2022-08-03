
import os
from flask import Flask
from flask_cors import cross_origin
from adrinator.api.Iadrinator_api import IAdrinatorServer


class Server:
    """
    Class for the gerencial server version API of the Adrinator project.
    """
    _app = Flask(__name__)
    _api: dict[str, dict[str, IAdrinatorServer]] = {}

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
        for version in cls._api.keys():
            for api in cls._api[version].keys():
                cls._api[version][api].init()

    # Flask capitalized the first letter of the method name.
    @cross_origin()
    @_app.route('/<path:path>', methods=['GET'])
    def manager(path: str):  # type: ignore
        """
        The method is used to greet the user.
        """

        # path to split the path in the url and get the API version
        path_split = [i for i in path.split('/') if i != '']

        match path_split[0:2]:
            case ['v1', 'github']:
                return Server._api['v1']['github'].get_request(path_split[2:])

            case ['production']:
                return {
                    'status': 'ok',
                    'production': Server.is_production()
                }

            case _:
                return {
                    'status': 'API not found'
                }

    @classmethod
    def run(cls, AdrinatorApps: dict[str, dict[str, IAdrinatorServer]]):
        # Instance of the AdrinatorAppV1 class.
        cls._api = AdrinatorApps

        # Initialize the APIs.
        cls._init_APIs()

        # Get port from environment variable or choose the default one.
        port = int(os.environ.get("PORT", 8000))

        # Run the server.
        cls._app.run(
            host='0.0.0.0',
            port=port,
            debug=not cls.is_production()
        )

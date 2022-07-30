import os
from adrinator.adrinator_server import Server

token = None
production = False

"""
This is the main file of the Adrinator project.
The try/except block is used to catch the exception raised when the token
is not provided. The token is used to authenticate the user in the GitHub API.
The production flag is used to determine if the server should run in production
mode or not.
"""
try:
    with open(os.path.join(os.path.dirname(__file__), 'token'), 'r') as f:
        print(os.path.join(os.path.dirname(__file__), 'token'))
        token = f.read()
except FileNotFoundError:
    token = os.environ.get('GH_API')

    if token is None:
        print('No token found. Please set GH_API environment.')
        exit(1)

    production = True

# the line below is used to run the server in production mode
Server.run(token, production=production)

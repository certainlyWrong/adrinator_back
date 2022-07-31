
import os
from adrinator.server import Server
from adrinator.api.v1.adrinator_api_v1 import Adrinator_GH_API_V1

# Configure and create a temporary directory for the files.
pathTempDir = f'{os.path.abspath(os.path.dirname(__file__))}/temp'

try:
    os.mkdir(pathTempDir)
except FileExistsError:
    pass

# the line below is used to run the server in production mode
Server.run(
    [Adrinator_GH_API_V1(pathTempDir)]
)

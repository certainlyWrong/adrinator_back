from abc import ABC, abstractmethod


class IAdrinatorServer(ABC):
    """
    Interfaces with the Iadrinator APIs This class
    is used to interact with the Iadrinator API.
    """

    @abstractmethod
    def get_request(self, requests: list[str]) -> dict:
        """
        The method is used to get the request from the API.
        """
        pass

    @abstractmethod
    def init(self) -> bool:
        """
        The method is used to initialize the API.
        """
        pass

from abc import ABC, abstractmethod


class IAdrinatorServer(ABC):
    """
    Interfaces with the Iadrinator APIs This class
    is used to interact with the Iadrinator API.
    """

    @abstractmethod
    def init(self) -> bool:
        """
        The method is used to initialize the API.
        """
        pass

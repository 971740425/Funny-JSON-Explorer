from abc import ABC, abstractmethod
from ..node import JSONNode
from ..icon import IconFamily

class StyledJSONNode:
    def __init__(self, root: JSONNode, icon_family: IconFamily) -> None:
        self._root = root
        self._icon_family = icon_family

    @abstractmethod
    def render(self) -> None:
        pass

class StyledJSONNodeFactory(ABC):
    @abstractmethod
    def create(self, root: JSONNode, icon_family: IconFamily) -> StyledJSONNode:
        pass
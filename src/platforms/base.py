from abc import ABC,abstractmethod
from src.models import ContentDraft
class PlatformAdapter(ABC):
    @abstractmethod
    def publish(self,draft:ContentDraft)->str: ...

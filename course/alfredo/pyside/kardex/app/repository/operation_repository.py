from abc import ABC, abstractmethod
from typing import Optional, List, Any

from course.alfredo.pyside.kardex.app.entity.operation import Operation


class OperationRepository(ABC):

    @abstractmethod
    def find_by_id(self, operation_id: int) -> Optional[Operation]:
        pass

    @abstractmethod
    def find_all(self, offset: int = 0, limit: int = 100) -> List[Operation]:
        pass

    @abstractmethod
    def save(self, operation: Operation) -> Operation:
        pass

    @abstractmethod
    def delete(self, operation_id: int) -> bool:
        pass
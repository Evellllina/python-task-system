from typing import Protocol, List, runtime_checkable
from .tasks import Task

@runtime_checkable
class TaskSourceProtocol(Protocol):
    """
    Протокол, определяющий обязательное поведение источников задач.
    Любой класс, который хочет быть источником задач в системе,
    должен реализоать метод get_tasks().
    """
    def get_tasks(self) -> List[Task]:
        ...
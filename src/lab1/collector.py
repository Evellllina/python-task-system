from typing import List
from .tasks import Task
from .protocols import TaskSourceProtocol

class TaskCollector:
    """
    Сборщик задач из различных источников.
    Класс принимает источники задач, проверяет их соответствие протоколу
    и собирает все задачи в единый список.

    """
    def __init__(self):
        self.sources =[]

    def add_source(self, source) -> None: #добавить источник в сборщик
        if not isinstance(source, TaskSourceProtocol):
            raise TypeError("Не реализует протокол TaskSourceProtocol")
        self.sources.append(source)
        print("Источник добавлен")

    def collect_all(self) -> List[Task]: #собрать все задачи из добавленных источников
        all_tasks = []
        for source in self.sources:
            tasks = source.get_tasks()
            all_tasks.extend(tasks)
            print(f"{source.__class__.__name__}: {len(tasks)} задач")
        return all_tasks

    def get_count(self) -> int: #количество добавенных источников
        return len(self.sources)

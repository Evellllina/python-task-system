from typing import List
from .tasks import Task
import json

class FileSource:
    """
    Файловый источник
    Читает задачи из файла в формате JSON и преобразует их в объекты Task

    """
    def __init__(self, filename: str):
        self.filename = filename
    def get_tasks(self) -> List[Task]:
        try:
            with open(self.filename, "r", encoding = "utf-8") as f:
                data = json.load(f)
            tasks = []
            for i in data:
                task = Task(
                    id=str(i.get('id', '')),
                    payload=i.get('payload', '')
                )
                tasks.append(task)
            return tasks
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден")
            return []
        except json.JSONDecodeError:
            print(f"Ошибка в файле {self.filename}")
            return []

class GeneratorSource:
    """
    Источник, который самостоятельно генерирует задачи

    """
    def __init__(self, count: int = 5, prefix: str = "generator"):
        self.count = count
        self.prefix = prefix
    def get_tasks(self) -> List[Task]:
        tasks = []
        for i in range(self.count):
            task = Task(
                id=f"{self.prefix}_{i}",
                payload=f"Тестовые данные {i}"
            )
            tasks.append(task)
        return tasks

class ApiSource:
    """
    Источник-заглушка
    Содержит заранее подготовленные тестовые данные,
    имитирующие ответ от внешнего API

    """
    def __init__(self):
        self.mock_data = [
            {"id": "api_1", "payload": {"user": "Alice", "action": "process"}},
            {"id": "api_2", "payload": {"user": "Kevin", "action": "review"}},
            {"id": "api_3", "payload": {"user": "Lola", "action": "approve"}},
        ]
    def get_tasks(self) -> List[Task]:
        tasks = []
        for i in self.mock_data:
            task = Task(
                id = i['id'],
                payload = i["payload"]
            )
            tasks.append(task)
        return tasks
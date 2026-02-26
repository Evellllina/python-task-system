class Task:
    """
    Класс в системе обработки задач
    Содержит уникальный индикатор и произвольные пользовские данные

    """

    def __init__(self, id: str, payload) -> None:
        if not isinstance(id, str) or not id:
            raise ValueError("id должен быть непустой строкой")
        self.id = id
        self.payload = payload

    def __repr__(self) -> str:
        return f"Task(id='{self.id}', payload = {self.payload})"

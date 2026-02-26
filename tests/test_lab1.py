import pytest
from src.lab1.tasks import Task
from src.lab1.protocols import TaskSourceProtocol
from src.lab1.sources import FileSource, GeneratorSource, ApiSource
from src.lab1.collector import TaskCollector

def test_generator_prefix0():
    gen = GeneratorSource(count=2, prefix="test")
    tasks = gen.get_tasks()
    assert tasks[0].id == "test_0"

def test_task_id():
    task = Task("123", "data")
    assert task.id == "123"

def test_task_payload():
    task = Task("123", "data")
    assert task.payload == "data"

def test_task_bad_id_pust():
    with pytest.raises(ValueError):
        Task("", "data")

def test_task_bad_id_str():
    with pytest.raises(ValueError):
        Task(123, "data")

def test_protocol_check_gen():
    assert isinstance(GeneratorSource(), TaskSourceProtocol)

def test_protocol_check_api():
    assert isinstance(ApiSource(), TaskSourceProtocol)

def test_protocol_check_file():
    assert isinstance(FileSource("test.json"), TaskSourceProtocol)

def test_collector_count():
    c = TaskCollector()
    c.add_source(GeneratorSource())
    c.add_source(ApiSource())
    assert c.get_count() == 2

def test_generator_prefix1():
    gen = GeneratorSource(count=2, prefix="test")
    tasks = gen.get_tasks()
    assert tasks[1].id == "test_1"

def test_generator_count():
    gen = GeneratorSource()
    tasks = gen.get_tasks()
    assert len(tasks) == 5

def test_generator_custom_count():
    gen = GeneratorSource(count=3)
    tasks = gen.get_tasks()
    assert len(tasks) == 3
    assert tasks[0].id == "generator_0"

def test_api_source_count():
    api = ApiSource()
    tasks = api.get_tasks()
    assert len(tasks) == 3

def test_api_source_content():
    api = ApiSource()
    tasks = api.get_tasks()
    assert tasks[0].id == "api_1"
    assert tasks[0].payload["user"] == "Alice"

def test_collector_add():
    c = TaskCollector()
    c.add_source(ApiSource())
    assert c.get_count() == 1

def test_file_bad_add():
    f = FileSource("test.json")
    tasks = f.get_tasks()
    assert tasks == []
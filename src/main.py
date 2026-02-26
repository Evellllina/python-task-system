from lab1.sources import GeneratorSource, ApiSource, FileSource
from lab1.collector import TaskCollector

collector = TaskCollector()

collector.add_source(GeneratorSource(count=3))
collector.add_source(ApiSource())
collector.add_source(FileSource("tasks.json"))

tasks = collector.collect_all()

print(f"\nВсего задач: {len(tasks)}")
for task in tasks:
    print(f"{task}")
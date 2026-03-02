from typing import Protocol, List, Any


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class AddStage:
    def __init__(self, value: int):
        self.value = value

    def process(self, data: Any) -> Any:
        return data + self.value


class MultiplyStage:
    def __init__(self, factor: int):
        self.factor = factor

    def process(self, data: Any) -> Any:
        return data * self.factor


class StringifyStage:
    def process(self, data: Any) -> Any:
        return str(data)


class Pipeline:
    def __init__(self, stages: List[ProcessingStage]):
        self.stages = stages

    def run(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data


if __name__ == "__main__":
    pipeline = Pipeline([
        AddStage(42),
        MultiplyStage(10),
        StringifyStage()
    ])

    print(pipeline.run(8))

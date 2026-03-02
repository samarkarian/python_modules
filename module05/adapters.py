from abc import ABC, abstractmethod
from typing import Protocol, List, Any


# --- Protocol pour les stages ---
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


# --- Stages ---
class AddStage():
    def __init__(self, value: int):
        self.value = value

    def process(self, data: Any) -> Any:
        return data + self.value


class MultiplyStage():
    def __init__(self, multi: int):
        self.multi = multi

    def process(self, data: Any) -> Any:
        return data * self.multi


class StringifyStage():
    def process(self, data: Any) -> Any:
        return str(data)


# --- Pipeline pour appliquer les stages ---
class Pipeline():
    def __init__(self, stages: List[ProcessingStage]):
        self.stages = stages

    def run(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data


# --- ABC pour les Adapters ---
class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


# --- Adapters avec gestion des stages et try/except ---
class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            for stage in self.stages:
                data = stage.process(data)
            return f"JSON processed: {data}"
        except Exception as e:
            return f"[JSONAdapter ERROR] {e}"


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            for stage in self.stages:
                data = stage.process(data)
            return f"CSV processed: {data}"
        except Exception as e:
            return f"[CSVAdapter ERROR] {e}"


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        try:
            for stage in self.stages:
                data = stage.process(data)
            return f"Stream processed: {data}"
        except Exception as e:
            return f"[StreamAdapter ERROR] {e}"


class NexusManager():
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def execute_all(self, data_list: List[Any]):
        for pipeline, data in zip(self.pipelines, data_list):
            result = pipeline.process(data)
            print(result)


# --- TEST ---
if __name__ == "__main__":
    # Pipeline avec stages
    pipeline = Pipeline([AddStage(5), MultiplyStage(2), StringifyStage()])
    print("Pipeline simple result:", pipeline.run(10))  # (10+5)*2 = 30 -> "30"

    # Adapters
    json_adapter = JSONAdapter("J1")
    csv_adapter = CSVAdapter("C1")
    stream_adapter = StreamAdapter("S1")

    # NexusManager
    manager = NexusManager()
    manager.add_pipeline(json_adapter)
    manager.add_pipeline(csv_adapter)
    manager.add_pipeline(stream_adapter)

    data_all = ["data1", "data2", "data3"]
    manager.execute_all(data_all)

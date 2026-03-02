from typing import List, Any


class ProcessingPipeline():
    def __init__(self):
        self.stages: List[Any] = []

    def add_stage(self, stage: Any):
        self.stages.append(stage)

    def process(self, data: Any):
        for stage in self.stages:
            data = stage.process(data)
        return (data)


class AddStage():
    def process(self, data: Any):
        data += 10
        return (data)


class MultiplyStage():
    def process(self, data: Any):
        data *= 2
        return (data)


class StringifyStage():
    def process(self, data: Any):
        data = str(data)
        return (data)


if __name__ == '__main__':
    pipeline = ProcessingPipeline()

    stage_list = [AddStage(), MultiplyStage(), StringifyStage()]

    for stage in stage_list:
        pipeline.add_stage(stage)

    print(pipeline.process(5))

from abc import ABC, abstractmethod


class HandsProcessor(ABC):
    @abstractmethod
    def process(self, hand_points: dict, eyes_points: dict):
        raise NotImplementedError("Este método debe ser implementado por una subclase")


from abc import ABC, abstractmethod

class FaceProcessor(ABC):
    @abstractmethod
    def process(self, points: dict):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

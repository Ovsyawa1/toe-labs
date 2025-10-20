from abc import ABC, abstractmethod


class AbstractCalculator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def write_to_csv():
        pass

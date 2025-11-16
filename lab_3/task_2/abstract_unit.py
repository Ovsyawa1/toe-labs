from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(
        self,
        name: str,
    ):
        self.name = name
        self.health = 0
        self.damage = 0
        self.defence = 0

    @abstractmethod
    def deal_damage():
        pass

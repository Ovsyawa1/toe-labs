from abstract_unit import Character
from abilities_classes import abl_dict


class Saber(Character):
    def __init__(self, name: str):
        health = 120
        damage = 10
        defence = 5
        strength = 5
        intelligence = 2
        agility = 2
        faith = 4

        # Передаем все хар-ки в конструктор Character/Unit
        super().__init__(name, health, damage, defence,
                         strength, intelligence, agility, faith)

        self.abilities = [abl_dict['dia'](), abl_dict['rakukaja']()]


class Assassin(Character):
    def __init__(self, name: str):
        health = 90
        damage = 12
        defence = 3
        strength = 4
        intelligence = 1
        agility = 7
        faith = 1

        super().__init__(name, health, damage, defence,
                         strength, intelligence, agility, faith)

        self.abilities = [abl_dict['cleave']()]


class Caster(Character):
    def __init__(self, name: str):
        health = 80
        damage = 8
        defence = 4
        strength = 1
        intelligence = 8
        agility = 3
        faith = 3

        super().__init__(name, health, damage, defence,
                         strength, intelligence, agility, faith)

        self.abilities = [
            abl_dict['agi'](),
            abl_dict['dia'](),
            abl_dict['marakunda']()
        ]


class Support(Character):
    def __init__(self, name: str):
        health = 110
        damage = 7
        defence = 6
        strength = 2
        intelligence = 3
        agility = 2
        faith = 7

        super().__init__(name, health, damage, defence,
                         strength, intelligence, agility, faith)

        self.abilities = [abl_dict['thermopylae'](), abl_dict['marakunda']()]

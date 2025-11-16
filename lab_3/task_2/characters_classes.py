from abstract_unit import Unit
from enemy_class import Enemy
from abilities_funtions import heal_char


class Character(Unit):
    def __init__(
        self,
        name: str,
    ):
        super().__init__(name)
        self.abilities = []
        self.strength = 0
        self.intelligence = 0
        self.agility = 0

    def deal_damage(self, enemy: Enemy):
        damage_multiplier = 1 + (0.8 * self.strength + 0.2 * self.agility)
        base_damage = self.damage - enemy.defence
        if base_damage <= 0:
            base_damage = 1
        enemy.health -= (base_damage * damage_multiplier)

    def use_ability(self):
        pass


class Saber(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 120
        self.damage = 10
        self.defence = 5
        self.strength = 5
        self.agility = 2
        self.intelligence = 2
        self.abilities = [heal_char]


Artur = Saber("Arhturia")
print(Artur.abilities)
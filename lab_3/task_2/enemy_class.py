from abstract_unit import Unit


class Enemy(Unit):
    def __init__(self, name, health, damage, defence):
        super().__init__(name, health, damage, defence)

    def deal_damage(self, enemy: Unit):
        enemy.health = enemy.health - self.damage + enemy.defence

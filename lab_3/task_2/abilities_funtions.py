from abstract_unit import Unit


def heal_char(ally: Unit, heal_value):
    ally.health += heal_value


def fireball(enemy: Unit, dmg_value):
    enemy.health = enemy.health - dmg_value + enemy.defence

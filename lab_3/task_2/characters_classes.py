from typing import List, Optional
from abstract_unit import Unit, Ability, Character


class Dia(Ability):
    def __init__(self):
        super().__init__("Dia")

    def execute(self, user: 'Character',
                target: Optional[Unit] = None, **kwargs):
        heal_target = target if target is not None else user
        heal_amount = heal_target.faith * 5 + 1
        heal_target.health += heal_amount
        print(
            f"[{self.name}] {user.name} "
            f"исцеляет {heal_target.name} на {heal_amount} HP."
        )


class Agi(Ability):
    def __init__(self):
        super().__init__("Agi")

    def execute(self, user: 'Character', target: Unit, **kwargs):
        damage_multiplier = user.intelligence
        base_damage = user.damage - target.defence
        if base_damage <= 0:
            base_damage = 1
        damage_dealt = base_damage * damage_multiplier
        target.health -= damage_dealt
        print(
            f"[{self.name}] {user.name}"
            f"наносит {damage_dealt:.2f} маг. урона {target.name}."
        )


class Rakukaja(Ability):
    def __init__(self):
        super().__init__("Rakukaja")

    def execute(self, user: 'Character', target: Unit, **kwargs):
        buff_amount = 5 + user.faith
        target.defence += buff_amount
        print(
            f"[{self.name}] {user.name} "
            f"увеличивает защиту {target.name} на {buff_amount}."
        )


class Cleave(Ability):
    def __init__(self):
        super().__init__("Cleave")

    def execute(self, user: 'Character', target: Unit, **kwargs):
        damage_multiplier = 1 + (user.agility * 0.9 + 0.1 * user.strength)
        base_damage = user.damage - target.defence
        if base_damage <= 0:
            base_damage = 1
        damage_dealt = base_damage * damage_multiplier
        target.health -= damage_dealt
        print(
            f"[{self.name}] {user.name} "
            f"наносит {damage_dealt:.2f} физ. урона {target.name}."
        )


class Thermopylae(Ability):
    def __init__(self):
        super().__init__("Thermopylae")

    def execute(self, user: 'Character', target: Unit, **kwargs):
        buff_amount = 5
        target.damage += buff_amount
        target.strength += buff_amount
        # и так далее для всех статов
        target.intelligence += buff_amount
        target.agility += buff_amount
        target.faith += buff_amount
        print(
            f"[{self.name}] {user.name} "
            f"баффает все статы {target.name} на {buff_amount}."
        )


class Marakunda(Ability):
    def __init__(self):
        super().__init__("Marakunda")

    def execute(self, user: 'Character',
                target_list: List[Unit] = None, **kwargs):
        if not target_list:
            print(f"[{self.name}] {user.name} использует, но нет целей.")
            return

        for enemy in target_list:
            enemy.defence -= 5
            if enemy.defence < 0:
                enemy.defence = 0
            print(f"  > Защита {enemy.name} снижена до {enemy.defence}.")


# Создадим псевдоним для удобства
abl_dict = {
    'dia': Dia,
    'rakukaja': Rakukaja,
    'cleave': Cleave,
    'agi': Agi,
    'thermopylae': Thermopylae,
    'marakunda': Marakunda
}

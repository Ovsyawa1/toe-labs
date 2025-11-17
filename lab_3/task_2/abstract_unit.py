from abc import ABC, abstractmethod
from typing import List, Optional


class Unit(ABC):
    """Базовый абстрактный класс для всех юнитов."""
    def __init__(
        self,
        name: str,
        health: int = 1,
        damage: int = 0,
        defence: int = 0,
        strength: int = 0,
        intelligence: int = 0,
        agility: int = 0,
        faith: int = 0,
    ):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.faith = faith

    @abstractmethod
    def deal_damage(self, target):
        pass


class Enemy(Unit):
    def __init__(self, name, health, damage, defence):
        super().__init__(name, health=health, damage=damage, defence=defence)

    def deal_damage(self, target):
        damage_taken = self.damage - target.defence
        if damage_taken < 1:
            damage_taken = 1
        target.health -= damage_taken


class Character(Unit):
    """Базовый класс персонажа. Умения определяются подклассами."""
    def __init__(self, name: str, health: int, damage: int, defence: int,
                 strength: int, intelligence: int, agility: int, faith: int):
        # Вызываем Unit.__init__ с полным набором статов
        super().__init__(name, health, damage, defence, strength,
                         intelligence, agility, faith)
        self.abilities: List[Ability] = []

    def deal_damage(self, enemy: Unit):
        damage_multiplier = 1 + (0.8 * self.strength + 0.2 * self.agility)
        base_damage = self.damage - enemy.defence
        if base_damage <= 0:
            base_damage = 1
        damage_dealt = base_damage * damage_multiplier
        enemy.health -= damage_dealt
        print(
            f"{self.name} наносит обычный удар {enemy.name} "
            f"на {damage_dealt:.2f} урона. ({enemy.health:.2f} HP осталось)"
        )

    def use_ability(
        self,
        abl_index: int,
        target: Optional[Unit] = None,
        target_list: Optional[List[Unit]] = None
    ):
        try:
            ability_object = self.abilities[abl_index]
            print(f"\n--- {self.name} активирует {ability_object.name} ---")

            ability_object.execute(
                user=self,
                target=target,
                target_list=target_list
            )

        except IndexError:
            print("Ошибка: Умение с таким индексом не найдено.")
        except Exception as e:
            print(f"Ошибка при использовании умения: {e}")


# Абстрактный класс умения
class Ability(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(
        self,
        user: 'Character',
        target: Optional[Unit] = None,
        target_list: Optional[List[Unit]] = None
    ):
        pass

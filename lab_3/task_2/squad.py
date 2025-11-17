from abstract_unit import Unit, Character
from typing import List


class Squad:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Character] = []

    # Добавить в отряд
    def add(self, char: Character):
        if char not in self.members:
            self.members.append(char)
            print(f"[{self.name}] {char.name} добавлен в отряд.")
        else:
            print(f"[{self.name}] {char.name} уже в отряде.")

    # Удалить из отряда
    def remove(self, char: Character):
        if char in self.members:
            self.members.remove(char)
            print(f"[{self.name}] {char.name} удалён из отряда.")
        else:
            print(f"[{self.name}] {char.name} не найден в отряде.")

    # Запринтить состав отряда
    def list_members(self):
        print(f"\n[{self.name}] Состав отряда:")
        if not self.members:
            print("  (пусто)")
            return 0
        for idx, m in enumerate(self.members):
            print(f"  {idx}. {m.name} (HP: {m.health:.1f})")

    # Есть живые члены отряда
    def alive_members(self) -> List[Character]:
        return [m for m in self.members if m.health > 0]

    # Живых не осталось :(
    def is_wiped(self) -> bool:
        return all(m.health <= 0 for m in self.members) or not self.members

    # //// Приказы отряду ////

    # Всем атаковать обычной атакой
    def order_attack_target(self, target: Unit):
        print(f"\n[{self.name}] Приказ: атаковать {target.name}!")
        for m in self.alive_members():
            m.deal_damage(target)
            if target.health <= 0:
                print(f"{target.name} повержен!")
                break

    # Сдаться
    def surrender(self):
        to_remove = []
        print("\nБыл отдан приказ сдаться. Все воины повержены...")
        for m in self.members:
            to_remove.append(m)
        for m in to_remove:
            self.remove(m)

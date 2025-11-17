
from abstract_unit import Enemy
from chars_classes import Saber, Assassin, Caster, Support
from squad import Squad


def run_test_scenario():
    print("/// Начало Тестового Забега Отряда ///")

    # 1. Инициализация Юнитов и Отряда
    # Создание персонажей разных классов
    saber = Saber("Артурия")
    assassin = Assassin("Хассан")
    caster = Caster("Мерлин")
    support = Support("Аоко")

    # Создание врагов
    goblin1 = Enemy("Гоблин-Берсерк", health=1000, damage=150, defence=2)
    goblin2 = Enemy("Гоблин-Маг", health=3000, damage=120, defence=1)
    goblin3 = Enemy("Гоблин-Танк", health=5000, damage=80, defence=10)
    enemy_squad = [goblin1, goblin2, goblin3]

    # Создание отряда
    our_squad = Squad("Dream Team")
    our_squad.add(saber)
    our_squad.add(assassin)
    our_squad.add(caster)
    our_squad.add(support)

    our_squad.list_members()

    print("\n--- Начальные характеристики ---")
    print(
        f"{saber.name}: HP={saber.health:.1f}, ATK={saber.damage}, "
        f"DEF={saber.defence}, STR={saber.strength}, FAI={saber.faith}"
    )
    print(
        f"{goblin1.name}: HP={goblin1.health:.1f}, ATK={goblin1.damage}, "
        f"DEF={goblin1.defence}"
    )

    # 2. Применение Баффов/Дебаффов (Групповые и Одиночные)
    # 2.1 Групповой дебафф (Marakunda)
    caster.use_ability(abl_index=2, target_list=enemy_squad)
    print(f"-> Защита {goblin1.name} после Marakunda: {goblin1.defence}")

    # 2.2 Групповой бафф (Thermopylae)
    support.use_ability(abl_index=0, target=saber)
    print(f"-> Сила {saber.name} после Thermopylae: {saber.strength}")

    # 2.3 Одиночный бафф (Rakukaja)
    saber.use_ability(abl_index=1, target=caster)
    print(f"-> Защита {caster.name} после Rakukaja: {caster.defence}")

    # 3. Боевые Действия
    print("\n--- Фаза Атаки ---")

    # 3.1 Обычная атака отряда по одному врагу
    our_squad.order_attack_target(goblin1)
    if goblin1.health > 0:
        print(f"-> {goblin1.name} выжил с HP: {goblin1.health:.2f}")

    # 3.2 Физическая способность (Cleave)
    if goblin2.health > 0:
        assassin.use_ability(abl_index=0, target=goblin2)
        print(f"-> {goblin2.name} HP: {goblin2.health:.2f}")
        if goblin2.health <= 0:
            print(f"{goblin2.name} повержен")

    # 3.3 Магическая способность (Agi)
    if goblin3.health > 0:
        caster.use_ability(abl_index=0, target=goblin3)
        print(f"-> {goblin3.name} HP: {goblin3.health:.2f}")
        if goblin3.health <= 0:
            print(f"{goblin3.name} повержен")

    # 3.4 Лечение (Dia)
    caster_hp_before = caster.health
    caster.use_ability(abl_index=1)
    print(
        f"-> {caster.name} HP до: {caster_hp_before:.2f}, "
        f"после: {caster.health:.2f}"
    )
    saber_hp_before = saber.health
    caster.use_ability(abl_index=1, target=saber)
    print(
        f"-> {saber.name} HP до: {saber_hp_before:.2f}, "
        f"после: {saber.health:.2f}"
    )

    # 4. Ответная атака врагов (Enemy.deal_damage)
    print("\n--- Ответная Атака Врагов ---")

    for enemy in enemy_squad:
        target_char = our_squad.alive_members()[0]
        if enemy.health > 0:
            enemy.deal_damage(target_char)
            print(
                f"-> {target_char.name} получил урон от {enemy.name}. "
                f"HP: {target_char.health:.2f} (Защита: {target_char.defence})"
            )

        # Проверка, если цель повержена
        if target_char.health <= 0:
            target_char.health = 0
            print(f"{target_char.name} был повержен!")
            if our_squad.is_wiped():
                print("--- ☠️ Отряд повержен! Конец забега. ---")
                return

    # 5. Проверка состояния
    print("\n/// Финальная сводка ///")
    our_squad.list_members()
    alive_enemies = [e for e in enemy_squad if e.health > 0]

    if not alive_enemies:
        print("--- Все враги повержены! ---")
    else:
        print(f"Враги, которые выжили: {[e.name for e in alive_enemies]}")
        print(f"Состояние отряда 'wiped': {our_squad.is_wiped()}")

    # 6. Демонстрация удаления члена отряда и сдачи (Surrender)
    if saber in our_squad.members:
        our_squad.remove(saber)

    our_squad.list_members()

    # Завершающий приказ
    our_squad.surrender()
    our_squad.list_members()


if __name__ == "__main__":
    run_test_scenario()

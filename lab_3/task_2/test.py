from abstract_unit import Enemy
from chars_classes import Saber, Caster, Support


saber_arturia = Saber("Артурия")
caster_medea = Caster("Медея")
support_merlin = Support("Мерлин")

goblin_1 = Enemy("Гоблин А", health=30, damage=5, defence=2)
goblin_2 = Enemy("Гоблин Б", health=30, damage=5, defence=2)
enemy_list = [goblin_1, goblin_2]

print(
    f"Name: {saber_arturia.name} | Health: {saber_arturia.health} | "
    f"Defence: {saber_arturia.defence}"
)
print(
    f"Name: {goblin_1.name} | Health: {goblin_1.health} | "
    f"Defence: {goblin_1.defence}\n"
)

# 1. Saber использует Rakukaja (индекс 1) на себе (Ally Buff)
saber_arturia.use_ability(abl_index=1, target=saber_arturia)
print(
    f"-> {saber_arturia.name} Defence после баффа: {saber_arturia.defence}\n"
)

# 2. Caster использует Marakunda (индекс 2) на всех врагах (AoE Debuff)
caster_medea.use_ability(abl_index=2, target_list=enemy_list)
print(f"-> {goblin_1.name} Defence после дебаффа: {goblin_1.defence}\n")

# 3. Caster использует Agi (индекс 0) на Гоблине А (Single Target Damage)
caster_medea.use_ability(abl_index=0, target=goblin_1)
print(f"-> {goblin_1.name} Health: {goblin_1.health:.2f}\n")

# 4. Support использует Thermopylae (индекс 0) на Saber (Ally Buff)
support_merlin.use_ability(abl_index=0, target=saber_arturia)
print(
    f"-> {saber_arturia.name} Strength после баффа: {saber_arturia.strength}\n"
)

from characters_classes import Character
from abilities_funtions import heal_char


artur = Character("Arthur", 80, 20, 10, [heal_char])

print(artur.health)

artur.abilities[0](artur, 20)

print(artur.health)

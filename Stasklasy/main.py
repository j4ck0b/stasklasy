from player import Player
from monster import Monster
from character import Character
from random import randint

opponents = [
    Monster("Goblin child", 5, randint(1,2), 0),
    Monster("Goblin adult", 10, randint(1,5), 1),
    Monster("Feral Dog", 5, randint(2,10), 2),
    Monster("Bear", 40, randint(10,20), 5),
    Monster("Bandit", 20, randint(5,10), 3),
    Monster("Animated decayed corpse", 60, randint(5,10), 4)
]

def random_opponent():
    return opponents[randint(0, len(opponents)-1)]

def pick_att(player, monster):
    print("a/A - Normal attack")
    print("b/B - Fireball")
    print("c/C - Strong punch")
    print("d/D - Smite")
    print("e/E - Vampiric drain")
    print("-"*40)
    what = input()
    match what.upper():
        case "A": return player.normal_att()
        case "B": return player.fireball()
        case "C": return player.strong_att()
        case "D": return player.smite()
        case "E": return player.vampiric_succ(monster)
        case _:   print("No option picked.")
    return 0

name = input("Hero name: ")
life = int(input("Life: "))
mana = int(input("Mana: ")) 
player = Player(name, life, mana)
while player.life > 0:
    monster = random_opponent()
    print("-"*40)
    while monster.hp > 0:
        print(f"{player.name} is faced with {monster.name}")
        print(f"Enemy has {monster.hp} HP and deals {monster.att} damage to you")
        player.life = player.life - monster.att
        if player.life <= 0: break
        print(f"You have {player.life} HP left and {player.mana} MP left")
        att = pick_att(player, monster)
        monster.hp = monster.hp - att
        print(f"You dealt {att} damage")
    if player.life <= 0: break
    print("-"*40)
    print("Opponent defeated!!!")
    player.amount_of_defeated_opponents += 1

print("-"*40)
print("Game Over!")
print("git gut")
print(f"You killed {player.amount_of_defeated_opponents} foes")
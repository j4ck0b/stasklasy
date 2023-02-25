from random import randint
from character import Character

class Player(Character):
    def __init__(self, name, life, mana):
        super().__init__(name, life, mana)
        self.amount_of_defeated_opponents = 0

    @staticmethod
    def normal_att():
        return randint(0,10)
    
    def fireball(self):
        if self.mana < 10:
            print("No Mana")
            return 0
        self.mana -= 10
        return randint(10,25)
    
    def strong_att(self):
        if self.life < 50: 
            print("You are exhausted")
            return 0
        return randint(5,15)

    def smite(self):
        if self.mana < 5:
            print("No Mana")
            return 0
        self.mana -= 5
        return randint(5,20)

    def vampiric_succ(self, monster):
        if self.life < monster.hp:
                print("You cant drain life from stronger opponent")
                return 0
        x = randint(5,10)
        self.life += x
        return x
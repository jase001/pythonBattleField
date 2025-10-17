import math
import random
from abc import ABC, abstractmethod


#CLASSES
class Character:
    mode = "beginner"
    counter = 0
    maxHealth=5
    def __init__(self, name, health, weapon, ability):
        Character.counter  +=1
        self.number = Character.counter
        self.name = name
        self.health = health
        self.weapon = weapon
        self.ability = ability

    def finisher(self):
        return "hard smash"   
    
    def attack(self):
        return f"{self.name} strikes"

    def heal(self):
        return f"adding +1 health {self.name}"
    def __str__(self):  #instance method
        return f" Player no[{self.number}] {self.name} current health is {self.health} with special ability {self.ability} and weapon {self.weapon}"

    def died(self):
        return self.maxHealth -1

    @classmethod   #changing game mode
    def gameMode(cls, mode):
        Character.mode = mode

    @staticmethod  
    def bio():
        print("custom made player")


class Healer:
    def __init__(self,potion, shield):
        self.potion = potion
        self.shield = shield

    def heal(self):
        return "adding +1 health to"


class Hero(Character):
    def __init__(self, name,health, weapon, ability, catchphrase, logo):
        super().__init__(name,health, weapon, ability)
        self.catchphrase = catchphrase
        self.logo = logo

    def finisher(self):
        return f"smash with a {self.weapon}"  

class Paladin(Healer, Hero):
    def __init__(self, name, weapon, ability, catchphrase, logo, potion, shield):
        
        Hero.__init__(self, name, weapon, ability, catchphrase, logo)
        Healer.__init__(self,potion, shield )


        

class Monster(ABC):      #abstract class
    @abstractmethod
    def roar(self):
        pass

    def record(self):
        return "undefeated throughout the underworld"

class Dragon(Monster, Healer):
    maxHealth=5
    _rage = ""
    def __init__(self, name, health, weight):
        self.name = name
        self.health = health
        self.weight = weight

    def roar(self):
        return f"{self.name} roared"
    
    def __str__(self):
        return self.record() + f"...{self.name} with health {self.health}"
    
    def heal(self):
        return super().heal() + f" {self.name}"
    # getter method
    @property
    def _rage(self):
        return self._rage
    
    # setter method
    @_rage.setter
    def set_rage(self, _rage):
        self._rage = _rage


#METHODS
def gamePlay(heroSet, vilian):
        max = len(hero) -1
        while max >=0 :
            b = (random.randint(0, max))
            temp = b 
            max-=1
            round0neGame(b,heroSet, vilian,roundTwoSet)
            #removing elements chosen in original list
            hero.remove(hero[b])
            vilian.remove(vilian[b])
            # print(vilian[b].__str__())


def round0neGame(b, heroSet, vilian, roundTwoSet):
    print("\nLET ROUND ONE BEGIN")
    while heroSet[b].health >0 and vilian[b].health>0 :
                moveToss()#determines whose move it is
                if moveToss() ==0:  
                    # determines type of play
                    if moveToss() ==0:  
                        print(heroSet[b].attack(), vilian[b].name, "with health", vilian[b].health)
                        vilian[b].health -=1
                    elif moveToss2()==3 and heroSet[b].health<heroSet[b].maxHealth:
                        print(heroSet[b].heal())
                        heroSet[b].health +=1

                elif moveToss()==1:
                    if moveToss() ==0:  
                        print(vilian[b].roar(), heroSet[b].name, "with health", heroSet[b].health)
                        heroSet[b].health -=1

                    elif moveToss2()==3 and vilian[b].health<vilian[b].maxHealth:
                        print(vilian[b].heal())
                        vilian[b].health +=1

    if hero[b].health > vilian[b].health :
        roundTwoSet.append(hero[b])
        print("round winner is", roundTwoSet[-1])
    else :
        roundTwoSet.append(vilian[b])
        print("round winner is", roundTwoSet[-1])


def final(roundTwoSet):
        print("\nLET ROUND TWO BEGIN")
        tempArr =[]
        
        while len(roundTwoSet)!=1:
            tempArr = roundTwoSet[:]   # creates a copy
            attacker = random.choice(roundTwoSet)
            # print(roundTwoSet[0].attack())
            toss = moveToss()  # determines type of play 
            if toss ==0:  
                        
                        tempArr.remove(attacker)
                        attackHit = random.choice(tempArr)
                        tempArr.append(attacker)
                        # print(attacker.name)

                       
                        if  isinstance(attacker, Hero):
                            print("with health", attacker.health, attacker.attack(), attackHit.name, "with health", attackHit.health)
                        elif isinstance(attacker, Dragon):
                            print("with health", attacker.health, attacker.roar(), attackHit.name, "with health", attackHit.health)
                        
                        roundTwoSet[roundTwoSet.index(attackHit)].health -=1
            elif toss ==1 and attacker.health<attacker.maxHealth:
                        print(attacker.heal())
                        roundTwoSet[roundTwoSet.index(attacker)].health +=1

            
            for a in roundTwoSet[:]:    
                if a.health == 0:
                    print(a.name," has been ELIMINATED")
                    roundTwoSet.remove(a)


def moveToss():
    return (random.randint(0, 1))
def moveToss2():
    return (random.randint(0, 3))


#CREATING OBJECTS
char1 = Hero("Sky",5, "boomerang", "flair", "GOTCHA", "lion crest")
char2 = Hero("Jinx", 5 ,"subMachine gun", "shape-shifter", "GOTCHA", "lion crest")
char3 = Hero("Vender", 5, "hammer","strength", "GOTCHA", "lion crest")    


vil1 = Dragon("Dragon1",5, "200lb")
vil2 = Dragon("Dragon2", 5 ,"150lb gun")
vil3 = Dragon("Dragon3", 5, "180lb")  
# print(char3.__str__())


hero = [char1, char2, char3]
vilian = [vil1,vil2,vil3]
roundTwoSet = []

print()
gamePlay(hero,vilian)   #round 1
print("array length is: ", len(roundTwoSet))                  
final(roundTwoSet)      #final round


for a in range(len(roundTwoSet)):
    if len(roundTwoSet)==1:
        print("\nWINNER for final round is :",roundTwoSet[a])



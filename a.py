import random
# My except
class Die(Exception):
    pass
class Finish(Exception):
    pass
class Clear(Exception):
    pass

# Pokemon abstract class
class Pokemon:
    def __init__(self, name, type, Lv, Hp, Deal):
        self.name = name
        self.type = type
        self.Lv = Lv
        self.Hp = Hp
        self.Deal = Deal
    def info(self):
        print(f"Name: {self.name}, Type: {self.type}, Lv: {self.Lv}, Hp: {self.Hp}, Deal: {self.Deal}")
    def Attack(self, target):
        print(f"{self.name} attack {target.name} by {self.type}type skill!")
        if self.type == 'Electric' or self.type == 'Psychic':
            print("Super-effective!!")
            target.Hp -= int(self.Deal * 1.2)
        elif self.type == 'Grass':
            if target.type == 'Water':
                print("Super-effective!!")
                target.Hp -= int(self.Deal * 1.2)
            elif target.type == 'Fire':
                print("Not very effective...")
                target.Hp -= int(self.Deal / 1.2)
            else:
                target.Hp -= self.Deal
        elif self.type == 'Fire':
            if target.type == 'Grass':
                print("Super-effective!!")
                target.Hp -= int(self.Deal * 1.2)
            elif target.type == 'Water':
                print("Not very effective...")
                target.Hp -= int(self.Deal / 1.2)
            else:
                target.Hp -= self.Deal
        elif self.type == 'Water':
            if target.type == 'Fire':
                print("Super-effective!!")
                target.Hp -= int(self.Deal * 1.2)
            elif target.type == 'Grass':
                print("Not very effective...")
                target.Hp -= int(self.Deal / 1.2)
            else:
                target.Hp -= self.Deal

# Evolution mixin class
class Evolution:
    def evol(self, n):
        print(f"Congratulations!Your {self.name}\nevolved into {n}")
        self.name = n
        self.Hp += 5
        self.Deal += 2

# Starting pokemon classes
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('Pikachu', 'Electric', 30, 71, 25)
class Turtwig(Pokemon, Evolution):
    def __init__(self):
        super().__init__('Turtwig', 'Grass', 10, 23, 11)
class Chimchar(Pokemon, Evolution):
    def __init__(self):
        super().__init__('Chimchar', 'Fire', 10, 23, 11)
class Piplup(Pokemon, Evolution):
    def __init__(self):
        super().__init__('Piplup', 'Water', 10, 23, 11)

# My Func
def isAdvanced(a, b) -> bool:
    if a.type == 'Electric' or a.type == 'Psychic':
        return True
    if a.type == 'Grass' and b.type == 'Water':
        return True
    if a.type == 'Water' and b.type == 'Fire':
        return True
    if a.type == 'Fire' and b.type == 'Grass':
        return True
    return False
def isEvolution(a, b) -> bool:
    if a.Lv >= b:
        return True
    return False

# main
Wild = ['Bidoof', 'Eevee', 'Magikarp', 'Squirtle', 'Ponyta', 'Roselia', 'Charmeleon', 'Gyarados', 'Torterra', 'Mewtwo']
w_Type = ['Normal', 'Normal', 'Water', 'Water', 'Fire', 'Grass', 'Fire', 'Water', 'Grass', 'Psychic']
p1 = Pikachu(); p2 = Turtwig(); p3 = Chimchar(); p4 = Piplup();
Starting = [p1, p2, p3, p4]

# set My_Pokemon
StartNum = int(input("Choose your starting Pokemon\n1) Turtwig   2) Chimchar   3) Piplup : "))
MyPokemon = Starting[StartNum]
print("Your starting Pokemon is", end= ' ')
MyPokemon.info()
print()

while True:
    # if flag is True you can run from wild Pokemon
    if StartNum == 0:
        flag = True
    else:
        flag = False

    # Evolution
    if isEvolution(MyPokemon, 25):
        if MyPokemon.name == 'Turtwig':
            MyPokemon.evol('Grotle')
            print()
        elif MyPokemon.name == 'Chimchar':
            MyPokemon.evol('Monferno')
            print()
        elif MyPokemon.name == 'Piplup':
            MyPokemon.evol('Prinplup')
            print()
    if isEvolution(MyPokemon, 55):
        if MyPokemon.name == 'Grotle':
            MyPokemon.evol('Torterra')
            print()
        elif MyPokemon.name == 'Monferno':
            MyPokemon.evol('Infernape')
            print()
        elif MyPokemon.name == 'Prinplup':
            MyPokemon.evol('Empoleon')
            print()

    # In Game
    try:
        if MyPokemon.Lv >= 100:
            raise Clear

        # set Wild_Pokemon
        if MyPokemon.Lv <= 20:
            WildNum = random.randint(0, 4)
        elif MyPokemon.Lv <= 50:
            WildNum = random.randint(5, 8)
        elif MyPokemon.Lv <= 80:
            WildNum = random.randint(7, 8)
        else:
            WildNum = random.randint(7, 9)

        if MyPokemon.Lv <= 30:
            WildLv = random.randint(MyPokemon.Lv - 5, MyPokemon.Lv + 3)
        elif MyPokemon.Lv <= 70:
            WildLv = random.randint(MyPokemon.Lv - 3, MyPokemon.Lv + 7)
        elif MyPokemon.Lv <= 93:
            WildLv = random.randint(MyPokemon.Lv, MyPokemon.Lv + 7)
        else:
            WildLv = 100

        WP = Pokemon(Wild[WildNum], w_Type[WildNum], WildLv, int(WildLv * 1.6) + 3, int(WildLv * 0.7) - 1)
        if WildNum == 9 and WildLv <= 90:
            WildLv += 5; WP.Hp += 8; WP.Deal += 10;
        print(f"Wild Pokemon {WP.name}(Lv.{WP.Lv}) is appeared!")

        # User select
        while True:
            MySelect = int(input(f"What will {MyPokemon.name} do?\n1) Fight   2) Run   3) Info   4) Quit : "))
            if MySelect == 1:
                MyPokemon.Attack(WP)
                if WP.Hp <= 0:
                    reward = int(WP.Lv * 0.05) + 1
                    MyPokemon.Lv += reward
                    MyPokemon.Hp += int(reward * 18.5) - 14
                    MyPokemon.Deal += int(reward * 0.9)
                    print(f"\n{WP.name} is dead\n{MyPokemon.name} get {reward}exp\n")
                    break
                WP.Attack(MyPokemon)
                print()
                if MyPokemon.Hp <= 0:
                    raise Die()

            elif MySelect == 2:
                if WP.Lv - MyPokemon.Lv <= 5 or flag:
                    print("You got away safely!\n")
                    break
                else:
                    flag = True
                    print("You couldn't get away!")
                    WP.Attack(MyPokemon)
                    print()
                    if MyPokemon.Hp <= 0:
                        raise Die()
            elif MySelect == 3:
                print("Your Pokemon:")
                MyPokemon.info()
                print("Wild Pokemon:")
                WP.info()
                if isAdvanced(MyPokemon, WP) and WildNum != 9:
                    print("Your Pokemon has advantaged!")

                if WP.Lv - MyPokemon.Lv <= 5 or flag:
                    print(f"You can run from {WP.name}\n")
                else:
                    print(f"You can't run from {WP.name}\n")
            elif MySelect == 4:
                raise Finish
            else:
                print("Please select a valid menu")

    # Exception handling
    except Die:
        s1 = "Your Pokemon is dead..."
        s2 = "Game Over"
        print(s1.center(20))
        print(s2.center(20))
        break
    except Finish:
        s1 = "Power is off"
        s2 = "See you next time~"
        print(s1.center(20))
        print(s2.center(20))
        break
    except Clear:
        s1 = "!!! Congraturation !!!"
        s2 = "You become a Pokémon Master."
        print(s1.center(30))
        print(s2.center(30))
        break
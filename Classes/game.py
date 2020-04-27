import random

class bgcolor:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKMAGENTA = "\033[35m"
    OKGREEN = "\033[92m"
    OKYELLOW = "\033[33m"
    OKLIGHTGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class Person:
    #attributes of the player
    def __init__(self, health_power, magic_power, attack_power, defence, magic, items):
        self.max_hp = health_power
        self.hp = health_power
        self.max_mp = magic_power
        self.mp = magic_power
        self.atk_low = attack_power - 10
        self.atk_high = attack_power + 10
        self.df = defence
        self.magic = magic
        self.actions = ["Attack", "Magic", "Portions"]
        self.item = items

    #random attack damage generated
    def get_atk_damage(self):
        self.atk_damage = random.randrange(self.atk_low, self.atk_high)
        return self.atk_damage

    #total damage to player or enemy
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        else:
            return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
         self.mp -= cost

    def choose_action(self):
        print(bgcolor.OKBLUE + bgcolor.BOLD + "------ACTIONS------" + bgcolor.ENDC)
        i = 1
        for items in self.actions:
            print("\t" + str(i), bgcolor.OKMAGENTA + items + bgcolor.ENDC)
            i += 1

    def choose_magic(self):
        i = 1
        for spells in self.magic:
            print("\t" + str(i), bgcolor.OKYELLOW+" "+str(spells.name)+" {cost: "+str(spells.cost) + "}" + bgcolor.ENDC)
            i += 1

    def choose_portion(self):
        i = 1
        for item in self.item:
            print("\t" + str(i), bgcolor.OKYELLOW + " " + str(item["item"].name) + " {cost: "+str(item["item"].cost) + "}" + " : " + str(item["quantity"]) + bgcolor.ENDC)
            i += 1
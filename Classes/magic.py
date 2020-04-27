import random

class Spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type

    # random magic damage generated
    def get_spell_damage(self):
        magic_low = self.damage - 5
        magic_high = self.damage + 5
        self.spell_damage = random.randrange(magic_low, magic_high)
        return self.spell_damage

from Classes.game import Person,bgcolor
from Classes.magic import Spell
from Classes.Items_Bag import Items

# magic options
# -----attack  magic-----
fire = Spell("Fire", 5, 10, "attack")
blast = Spell("Blast", 15, 15, "attack")
cannon = Spell("Cannon", 20, 20, "attack")
blaze = Spell("Blaze", 10, 10, "attack")
double_blade = Spell("Double_Blade", 25, 25, "attack")
thunderstruck = Spell("ThunderStruck", 20, 30, "attack")
tornado = Spell("Tornado", 30, 25, "attack")

# -----healing magic-------
small_Heal = Spell("Small Heal", 15, 20, "heal")
big_Heal = Spell("Big Heal", 30, 40, "heal")

# player Magic
player_magic = [fire, blast, blaze, tornado, small_Heal, big_Heal]
enemy_magic = [fire, blast, blaze, tornado]

# inventory or bag items
venom = Items("Venom", 20, 30, "attack", )
spitterz = Items("Spitterz", 10, 15, "attack")
elixir = Items("Elixir", 40, 30, "heal")

# player inventory
player_bag = [{"item": venom, "quantity": 2},
              {"item": spitterz, "quantity": 2},
              {"item": elixir, "quantity": 1}]

# enemy inventory
enemy_bag = []

# instantiating the players
player = Person(100, 100, 40, 30, player_magic, player_bag)
enemy = Person(200, 200, 20, 50, enemy_magic, enemy_bag)

print(bgcolor.BOLD + "NAME              HP                                  MP" + bgcolor.ENDC)
print(bgcolor.BOLD + "SAM:       " + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bgcolor.ENDC + bgcolor.OKLIGHTGREEN + "|█████████████████████████|" + bgcolor.ENDC + "  " + bgcolor.BOLD + str(player.get_mp()) + "/" + str(player.get_max_hp()) + bgcolor.OKBLUE + "|█████|" + bgcolor.ENDC)
print(bgcolor.BOLD + "NIKHIL:    " + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bgcolor.ENDC + bgcolor.OKLIGHTGREEN + "|█████████████████████████|" + bgcolor.ENDC + "  " + bgcolor.BOLD + str(player.get_mp()) + "/" + str(player.get_max_hp()) + bgcolor.OKBLUE + "|█████|" + bgcolor.ENDC)
print(bgcolor.BOLD + "SID:       " + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bgcolor.ENDC + bgcolor.OKLIGHTGREEN + "|█████████████████████████|" + bgcolor.ENDC + "  " + bgcolor.BOLD + str(player.get_mp()) + "/" + str(player.get_max_hp()) + bgcolor.OKBLUE + "|█████|" + bgcolor.ENDC)

print(bgcolor.FAIL+bgcolor.BOLD+"AN ENEMY IS ABOUT TO ATTACK"+bgcolor.ENDC)
print("====================================")

running = True
i = 0

# Game Starts
while running:
    player.choose_action()
    choice = int(input("Enter your Move no: "))
    choice -= 1
    current_mp = player.get_mp()
    # power attacks
    if choice == 0:
        dmg = player.get_atk_damage()
        enemy.take_damage(dmg)
        print("You attacked the enemy with", dmg, " points")

    # magic attacks
    elif choice == 1:
        player.choose_magic()
        magic_move = int(input("Enter your Choice no: "))
        magic_move -= 1
        spell = player.magic[magic_move]
        spell_name = spell.name

        if current_mp >= spell.cost:
            dmg = spell.get_spell_damage()
            if spell.type == "attack":
                enemy.take_damage(dmg)
                print("You attacked the enemy with", spell_name, " for ", dmg, " points")
            if spell.type == "heal":
                player.heal(dmg)
                print(bgcolor.OKMAGENTA+"You healed with", spell_name, " for ", dmg, " points"+bgcolor.ENDC)

        player.reduce_mp(spell.cost)

        if current_mp < spell.cost:
            print(bgcolor.FAIL + bgcolor.BOLD + "You cannot use", spell.name, "cause you don't have enough magic left" + bgcolor.ENDC)
            continue

    elif choice == 2:
        player.choose_portion()
        potion_move = int(input("Enter your Choice no: "))
        potion_move -= 1
        potion = player.item[potion_move]["item"]
        potion_name = potion.name
        dmg = potion.damage
        capacity = player.item[potion_move]["quantity"]

        if capacity != 0 and current_mp>= potion.cost:
            if potion.property == "attack":
                enemy.take_damage(dmg)
                print("You attacked the enemy with", potion_name, " for ", dmg, " points")
            if potion.property == "heal":
                player.heal(dmg)
                print(bgcolor.OKMAGENTA + "You healed with", potion_name, " for ", dmg, " points" + bgcolor.ENDC)

        capacity -= 1
        player.item[potion_move]["quantity"] = capacity

        if capacity < 0:
            print(bgcolor.FAIL + bgcolor.BOLD + "You used all of", potion_name + bgcolor.ENDC)
            continue

        player.reduce_mp(potion.cost)

        if current_mp < potion.cost:
            print(bgcolor.FAIL + bgcolor.BOLD + "You cannot use", potion.name, "cause you don't have enough magic left" + bgcolor.ENDC)
            continue

    # enemy attack
    dmg_1 = enemy.get_atk_damage()
    player.take_damage(dmg_1)
    print("The enemy attacked you with", dmg_1, " points")

    # player properties
    print("-----------------------------------")
    print(bgcolor.OKBLUE + "Player HP:" + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bgcolor.ENDC)
    print(bgcolor.OKBLUE + "Enemy HP:" + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bgcolor.ENDC, "\n")

    if current_mp <= 0:
        print(bgcolor.OKYELLOW + "Player MP: 0" + bgcolor.ENDC)
    else:
        print(bgcolor.OKYELLOW + "Player MP:" + str(player.get_mp()) + bgcolor.ENDC)
    print("-----------------------------------")

    # Decision of the winner
    if player.get_hp() == 0:
        print(bgcolor.FAIL + bgcolor.BOLD + "=========ENEMY WINS=========" + bgcolor.ENDC)
        running = False
    elif enemy.get_hp() == 0:
        print(bgcolor.OKGREEN + bgcolor.BOLD + "=========PLAEYER WINS=========" + bgcolor.ENDC)
        running = False

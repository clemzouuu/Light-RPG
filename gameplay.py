name = None 
from random import randint 

def game():
    name = (input('Quel est votre pseudo ?'))
    print('\n')
    print("""
    Te voici au sein d'Haïdar... le monde des rêves et de la magie. Là où tout est possible.
    À toi de parcourir ce monde afin d'en devenir le maitre.
    Néanmois, un long chemin d'embûches t'attendent tout le long de cette aventure.
    Bon courage à toi""", name)
    print('\n')
    world()

world_map = [
[ 'ᕦ(ˇò_ó)ᕤ','_','_','_','_'], 
['_','_','_','_','_'], 
['_','_','_','_','_']
]

def world():
    print("""
    Tu es sur le 1er continent, le continent paisible.
    Essaie de te rendre au bout du 3eme continent sans mourir.
    Pour avancer de pays en pays, entre '+1' quand il te sera demandé d'avancer. 
    """)
    print('\n')
    move_map()

Inventaire = []

def move_map():
    x = 0
    i = 0
    print(world_map)
    while x < 4 :
        print("Tu peux avancer.")
        answer = input()
        print("   ")
        if answer == '+1':
            world_map[0][i+1] = 'ᕦ(ˇò_ó)ᕤ'
            world_map[0][i] = '_'
            print("   ")
            if x == 0 :
                print("   ")
                print("Rien à signaler ici.")
            if x == 1 :
                print('\n')
                print("Un animal sauvage vient de t'effrayer, fais attention la prochaine fois.")
            if x == 2:
                print('\n')
                print('Tu viens de ramasser un bâton. Il te servira sûrement.')
                print('\n')                
                Inventaire.append('bâton')
            print(world_map)
            i = i +1
            x = x +1
        while answer != '+1':
            print("Réésaie.")
            answer = input()
    combat_1()

def combat_1():
    print('\n')
    print('ᕦ(ˇò_ó)ᕤ ⚔ ٩༼❦‿❦༽۶')
    print('\n')
    print("Voilà ton premier adversaire. Utilise ton bâton en ecrivant 'ATQ' pour l'achever.")

    attaque = input()
    while attaque != 'ATQ':
        print("Réésaie.")
        attaque = input()
    if attaque == 'ATQ':
        print("Bravo, tu as battu l'ennemi.")
        print('\n')
    monde_2()


def monde_2():
    print('\n')
    print("Tu peux accéder au 2eme continent, celui du brouillard.")
    print('Dans ton inventaire tu as',Inventaire)
    print("Tu peux avancer.")
    print('\n')
    world_map[1][0] = 'ᕦ(ˇò_ó)ᕤ'
    world_map[0][4] = '_'
    print(world_map)
    x = 0
    i = 0

    while x < 4:
        print('\n')
        answer = input()
        if answer == '+1':
            world_map[1][i+1] = 'ᕦ(ˇò_ó)ᕤ'
            world_map[1][i] = '_'
            if x == 0 or x == 2  or x ==4 :
                print("Fais attention, mais tu peux avancer.")
            if x == 1 :
                print('\n')
                print("Tu as ramassé une épée.")
                Inventaire.append('épée')
            if x == 3:
                print('\n')
                print("Tu as ramassé un sabre. Il remplace le bâton.")
                Inventaire.append('sabre')
                Inventaire.remove('bâton')
            print(world_map)
            i = i +1
            x = x +1
        while answer != '+1':
            print("Réésaie.")
            answer = input()
    combat_2()

def combat_2():
    print('\n')
    print('ᕦ(ˇò_ó)ᕤ ⚔ ٩༼❦‿❦༽۶')
    print('\n')
    print("Un adversaire ! Entre ATQ pour utiliser une arme contre l'adversaire.")
    attaque = input()
    while attaque != 'ATQ':
        print("Réésaie.")
        attaque = input()
    if attaque == 'ATQ':
        print('\n')
        print("Bravo, tu l'as achevé avec ton épée mais elle s'est brisée...Tu peux acceder au 3eme continent.")
        Inventaire.remove('épée')
    print('\n')
    monde_3()

def monde_3():
    print('\n')
    print("Te voici sur le dernier continent, celui du chaos...")
    print("Avance avec vigilence.")
    print('\n')
    x = 0
    i = 0
    world_map[2][0] = 'ᕦ(ˇò_ó)ᕤ'
    world_map[1][4] = '_'
    print(world_map)
    while x < 4:
        if x == 0 :
            combat_3()
        answer = input()
        if answer == '+1':
            world_map[2][i+1] = 'ᕦ(ˇò_ó)ᕤ'
            world_map[2][i] = '_'
            if x == 1 :
                print('\n')
                print("Un séisme de magnétude 9 vient de se faire sentir...Avance avec vigilence.")
                print('\n')
            if x == 2 :
                combat_3()
            if x == 3 :
                print("Fais très attention")
                print('\n')
            if x == 4 :
                print("Un immeuble vient de s'effonder à côté de toi, fais très attentino en avançant.")
                print('\n')
            print(world_map)
            i = i +1
            x = x +1
        while answer != '+1':
            print("Réésaie.")
            answer = input()
    print('\n')
    combat_4()

def combat_3():
    print('\n')
    print('ᕦ(ˇò_ó)ᕤ ⚔ ٩༼❦‿❦༽۶')
    print('\n')
    print("Un adversaire ! Entre ATQ pour utiliser une arme contre lui.")
    print('\n')
    print('Tu possède dans ton inventaire ',Inventaire)
    print('\n')
    attaque = input()
    while attaque != 'ATQ':
        print("Réésaie.")
        attaque = input()
    if attaque == 'ATQ':
        print('\n')
        print("Bravo, tu l'as achevé avec ton sabre tu peux continuer à avancer.")
    print('\n')

def combat_4():
    print('\n')
    print("Voici un très grand monstre ! Entre ATQ pour utiliser une arme contre lui. Plusieurs coups seront nécessaires.")
    print('Tu possède dans ton inventaire ',Inventaire)
    print('\n')
    for i in range(3):
        attaque = input()
        while attaque != 'ATQ':
            print("Réésaie.")
            attaque = input()
        if attaque == 'ATQ':
            print('\n')
            print("Tu viens de l'attaquer avec ton sabre. Entre ATQ pour continuer à l'attaquer." )
            print('\n')
            print('ᕦ(ˇò_ó)ᕤ ⚔ ٩༼❦‿❦༽۶')
        print('\n')
    
    print("Bravo, ce fut difficile mais tu es maintenant maitre de ce monde !!! ᕦ(ˇò_ó)ᕤ ")
    print('\n')


from gameplay import *

first_input = ('')

def main():
    menu()

def menu():
    print('\n')
    print('Bienvenue, veuillez choisir une option.')
    print('\n')
    print('Nouvelle partie')
    print('\n')
    print('Crédit')
    print('\n')
    print('Quit')
    print('\n')
    print('Entrez 1 pour Nouvelle partie, 2 pour Crédit, et 3 pour Quit.')
    print('\n')
    first_input = input()
    answer_menu(first_input)

def answer_menu(x):
    if x == '1' :
        start()

    elif x == '2':
        credit()

    elif x == '3':
        quit()
    else :
        print('\n')
        print("Erreur, les valeurs à rentrer son 1, 2 ou 3. Veuillez relancer le jeu.")
        quit()


def start():
    print('\n')
    print('Le jeu peut commencer.')
    print('\n')
    game()

def credit():
    print('\n')
    print('Le jeu a été fait par KINSIONA MFINDA Clément.')
    print('-----------------------------------------------')
    menu()

def quit():
    print('\n')
    print('Au revoir :)')
    print('\n')

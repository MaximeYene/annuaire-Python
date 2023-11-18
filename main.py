from PackageFonctions.fonctions import *
from PackageFonctions.messages import ajout_message


while True:
    print('Que souhaitez vous faire? ')
    print('1.Ajouter un contact')
    print('2.Supprimer un contact')
    print('3.Rechercher un contact')
    print('4.Modifier un contact')
    print('5.Afficher l annuaire')
    print('6.Ajouter un message')
    print('7.Quitter')

    choix=input('Entrez votre choix ')
    match choix:
        case '1':
            ajouter_contact()
        case '2':
            supprimer_contact()
        case '3':
            rechercher_contact()
        case '4':
            modifier_contact()
        case '5':
            afficher_tous_les_contacts()
        case '6':
            ajout_message()
        case '7':
            break


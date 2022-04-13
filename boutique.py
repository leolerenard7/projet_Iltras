import csv
import codecs
from colorama import Fore,Style,Back
from gestion_inventaire import *

def obj():
    T_obj_1=[]
    with codecs.open('liste_objets.csv','r') as csvfile:
        r=csv.DictReader(csvfile,delimiter=',')
        for row in r:
            T_obj_1.append(dict(row))
        return T_obj_1



liste_complete = [
    [elt[0] for elt in recup_objet(nom=None, all=True) if elt[17] == 0], [elt[0] for elt in recup_objet(nom=None, all=True) if elt[17] == 1],
    [elt[0] for elt in recup_objet(nom=None, all=True) if elt[17] == 2], [elt[0] for elt in recup_objet(nom=None, all=True) if elt[17] == 3],
    [elt[0] for elt in recup_objet(nom=None, all=True) if elt[17] == 4]
]

objets = recup_objet(all=True)
inventaire = afficher_inventaire()
inventaire_classic = afficher_inventaire(classic=True)

def boutique_main():
    achetable_0=[elt[0] for elt in recup_objet(nom=None, all=True) if elt[17] == 0]
    return achetable_0

def boutique_capit():
    achetable_1=[e['ind'] for e in objets if (int(e['Bouti-achet']) == 1)]
    return achetable_1

def boutique_port():
    achetable_2=[e['ind'] for e in objets if (int(e['Bouti-achet']) == 2)]
    return achetable_2

def boutique_jungle():
    achetable_3=[e['ind'] for e in objets if (int(e['Bouti-achet']) == 3)]
    return achetable_3

def boutique_volcan():
    achetable_4=[e['ind'] for e in objets if (int(e['Bouti-achet']) == 4)]
    return achetable_4

def vente(boutique):
    afficher_inventaire(classic=True)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    choix_vente = -999
    while (choix_vente > len(list(inventaire)) or choix_vente <= 0):
        try:
            choix_vente = int(input("Que voulez vous vendre ? | Choisissez l'objet ou tapez -1 pour annuler. -> "))
            break
        except ValueError:
            print(Fore.RED + "Vous devez entrer un nombre!")
    if choix_vente == -1:
        boutique_debut(boutique)
    else:
        if inventaire != []:
            if inventaire[choix_vente-1] in inventaire_classic:
                nom_choix = inventaire[choix_vente-1]
                T=[S for S in objets] #Tableau de tout les noms d'objet de 0 à indice max
                objet_utilise="0"
                for e in range(len(T)):
                    if T[e][1] == nom_choix[1]:
                        T[e][1]= objet_utilise
                        i = e #L'indice i de l'objet
                        if objets[i]['vendable'] == "1":
                            quantitee = 10000
                            while ((quantitee > inventaire[nom_choix]) or (quantitee < 0)):
                                try:
                                    quantitee = int(input("Combien de cet objet voulez vous vendre ? -> "))
                                except ValueError:
                                    print("Vous devez entrer un nombre!")
                                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                            if quantitee > 0:
                                if nom_choix in inventaire:
                                    if (inventaire[nom_choix] - quantitee) >= 0:
                                        inventaire[nom_choix] -= quantitee
                                        print(quantitee, nom_choix, "ont été vendu.")
                                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                        stat['argent'] = int(stat['argent']) + (quantitee * (int(objets[i]['valeur'])-(5/100)*int(objets[i]['valeur'])))
                                        print("Vous avez maintenant ",stat['argent']," pièces.")
                                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                                        if inventaire[nom_choix] == 0:
                                            del inventaire[nom_choix]
                                        vente(boutique,stat,inventaire,arme,armure)
                                    else:
                                        print("Vous ne pouvez pas vendre plus que ce que vous avez!")
                                        vente(boutique,stat,inventaire,arme,armure)
                                else:
                                    print("L'objet que vous voulez vendre n'est pas en votre possession...")
                                    boutique_debut(boutique,stat,inventaire,arme,armure)
                            else:
                                print("Vous ne pouvez pas vendre un nombre négatif d'objets, ou 0 objet!")
                                boutique_debut(boutique,stat,inventaire,arme,armure)
                        else:
                            print("Cet objet n'est pas vendable en boutique...")
                            vente(boutique,stat,inventaire,arme,armure)
        else:
            print("Vous n'avez aucun objet sur vous...")
            boutique_debut(boutique,stat,inventaire,arme,armure)



from inventaire import inventory_main
def boutique_debut(boutique,stat,inventaire,arme,armure):
    objets = obj()
    if boutique == 0:
        boutique_indice = boutique_main()
        boutique_noms = [e["nom"] for e in objets if (int(e['Bouti-achet']) == 0)]
        greetings = "Bonjour, je vous souhaite la bienvenue dans ma modeste auberge, John à votre service! "
        goodbye = "Un vent de changement souffle, je le sens arriver."
    elif boutique == 1:
        boutique_indice = boutique_capit()
        boutique_noms = [e["nom"] for e in objets if (int(e['Bouti-achet']) == 1)]
        greetings = "Bien le bonjour aventurier! Et bienvenue à la plus grande boutique de la capitale! Prenez le temps de décider ce que vous voulez faire et revenez à moi!"
        goodbye = "Bonne chance, dehors, les temps sont durs!"
    elif boutique ==2:
        boutique_indice = boutique_port()
        boutique_noms = [e["nom"] for e in objets if (int(e['Bouti-achet']) == 2)]
        greetings = "Hééé! Oohhh! YYYAARGHHH Jeune mousse, que m'veux tu? "
        goodbye = "Bonne chance sur les mers déchaînés YAAARGHHHH!"
    elif boutique  == 3:
        boutique_indice = boutique_jungle()
        boutique_noms = [e["nom"] for e in objets if (int(e['Bouti-achet']) == 3)]
        greetings = "Bonsoir, je serai votre vendeur pour aujourd'hui, vous pouvez m'appeler Rambo."
        goodbye = "Faites attention, la jungle peut s'avérer très dangereuse!"
    elif boutique == 4:
        boutique_indice = boutique_volcan()
        boutique_noms = [e["nom"] for e in objets if (int(e['Bouti-achet']) == 4)]
        greetings = "HEYYY, T'AS PAS UN PEU TROP CHAUD? T'AIMERAIS QUOI?"
        goodbye = "A BIENTÔT, SI TU NE FINIS PAS GRILLÉ D'ICI LA AHAHAHAHAHAHAHAH"
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(greetings)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Comment pourrais-je vous aider ?")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("1. ACHETER")
    print("2. VENDRE")
    print("3. PARTIR")
    print("4. INVENTAIRE ")
    choix_march = 0
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    while ((choix_march) !=1) and ((choix_march)!=2) and ((choix_march) != 3) and ((choix_march != 4)):
        try:
            choix_march=int(input("Bon j'ai une livraison qui m'attend. Que puis-je faire pour vous ? 1- Acheter 2- Vendre 3- Partir 4- Inventaire ->"))
        except ValueError:
            print(Fore.RED + "Tapez 1,2,3 ou 4!!!")
            print(Style.RESET_ALL)
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    if choix_march == 1:
        print("Cela tombe bien je viens de recevoir de nouveaux articles qui vont surement vous plaire !")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Voici ce que vous pouvez acheter :     | Vous avez",stat['argent'],"pièces.")
        for i in range(len(boutique_noms)):
            print(i+1," - ",boutique_noms[i], " : ", objets[int(boutique_indice[i])]['valeur']," pièces l'unité.")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        choix_acheter = -500
        while choix_acheter < -1 or choix_acheter == 0 or choix_acheter > len(boutique_noms):
            try :
                choix_acheter = int(input("Que voulez vous acheter? (Entrez le numéro correspondant ou tapez -1 pour revenir en arrière) ->"))
            except ValueError or (choix_acheter > len(boutique_noms) or choix_acheter < -1):
                print(Fore.RED + "Veuillez entrer le nombre d'un des produits présent dans la boutique.")
                print(Style.RESET_ALL)
        if choix_acheter == -1:
            boutique_debut(boutique,stat,inventaire,arme,armure)
            return -1    
        indice = int(boutique_indice[choix_acheter-1])
        print("Choix :", objets[indice]["nom"])
        valeur_indice = (objets[indice][('valeur')])
        print("Prix à l'unité:",(objets[indice][('valeur')])," pièces ")
        choix_nom = (objets[indice]["nom"])
        achetes = -5
        while ((achetes != 1) or (achetes != 2)):
            try:
                achetes=int(input("Voulez vous vraiment acheter ceci ? \n1: OUI \n2: NON\n-> "))
                if ((achetes == 1) or (achetes == 2)):
                    break
            except ValueError:
                print(Fore.RED + "Tapez 1 ou 2 uniquement!")
                print(Style.RESET_ALL)
        if achetes == 1:
            choix_fait_quantitee = -1
            while choix_fait_quantitee == -1:
                quantitee_ac = -5
                while quantitee_ac < 0:
                    try:
                        quantitee_ac = int(input("Combien de cet objet voulez vous acheter ? -> "))
                    except ValueError:
                        print(Fore.RED + "Tapez un nombre au dessus ou égal à 0!")
                        print(Style.RESET_ALL)
                if quantitee_ac == 0:
                    choix_fait_quantitee = 1
                elif stat['argent'] >= (int(valeur_indice)*quantitee_ac):
                    stat['argent'] = int(stat['argent']) - (int(valeur_indice)*quantitee_ac)
                    if choix_nom in inventaire:
                        inventaire[choix_nom] = inventaire[choix_nom]+1
                        choix_fait_quantitee = 1
                    else:
                        if quantitee_ac >0:
                            inventaire[choix_nom]=quantitee_ac
                        print("Votre inventaire :", inventaire)
                        print("Votre monnaie restante:", stat['argent'])
                        choix_fait_quantitee = 1
                else:
                    print("Vous n'avez pas assez de monnaie pour acheter ",quantitee_ac, choix_nom)
                    choix_fait_quantitee = -1
            boutique_debut(boutique,stat,inventaire,arme,armure)
        elif achetes == 2:
            print("Alors que faites vous ici?! Vous achetez quelque chose ou vous vous en allez, vous faites fuir les clients.")
            boutique_debut(boutique,stat,inventaire,arme,armure) 
            choix_fait=1
    elif choix_march == 2:
        vente(boutique,stat,inventaire,arme,armure)
    elif choix_march == 3:
        print(goodbye)
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        return -1
    elif choix_march == 4:
        inventory_main(0,stat,inventaire,arme,armure)
        boutique_debut(boutique,stat,inventaire,arme,armure)
    return -1

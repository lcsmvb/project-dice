import random 
from random import choices
from collections import Counter

SCORES = {
    "Pentagone": 100,
    "Carré": 60,
    "Full": 40,
    "Quinte": 35,
    "Brelan": 25,
    "Double paire": 15,
    "Paire": 8,
    "Dé haut": 2,
}

def lancerUnDe(n):
    d = random.randint(1,n)
    return d

def lancerDeDes(nbDes,nbFaces):
    listeDesDes = []    #la liste des dés, pour l'instant  vide
    for i in range(nbDes):
        d = lancerUnDe(nbFaces) #on lance un dé
        listeDesDes.append(d)     #on ajoute ce dé à la liste
    return listeDesDes

def sommeDeDes(nbDes,nbFaces):
    S = 0    #somme des dés, pour l'instant nulle
    for i in range(nbDes):
        d = lancerUnDe(nbFaces) #on lance un dé
        S=S+d     #on ajoute ce dé à la somme
    return S

def relancerDes(listeDesDes, indices, nbFaces=6):
    for i in indices:
        listeDesDes[i] = lancerUnDe(nbFaces)  # on relance seulement ce dé
    return listeDesDes

def reconnaitreMain(listeDesDes):
    compte = Counter(listeDesDes)                       # ex : [3,6,1,6,2] -> {6:2, 3:1, 1:1, 2:1}
    occurrences = sorted(compte.values(), reverse=True)  # ex : [2, 1, 1, 1]
    valeurs = sorted(set(listeDesDes))

des = lancerDeDes(5, 6)
print("Tes dés :", des)

choix = input("Lesquels relancer ? (ex : 1 3 5, ou Entrée pour aucun) : ")

if choix.strip():
    indices = [int(n) - 1 for n in choix.split()]  # le joueur tape 1 à 5, la liste va de 0 à 4
    des = relancerDes(des, indices)

print("Nouveaux dés :", des)
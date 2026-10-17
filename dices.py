import random 
from random import choices

## https://emilypython.wordpress.com/2018/03/14/lancons-des-des-avec-le-module-random-de-python/

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

 def somme_de_deux_dés() -> int:
    #https://www.xoolive.org/python/structures/jeux_de_des
    # on tire 2 dés, on fait la somme
    return sum(choices(faces, k=2))

des = lancerDeDes(5, 6)
print("Tes dés :", des)

choix = input("Lesquels relancer ? (ex : 1 3 5, ou Entrée pour aucun) : ")

if choix.strip():
    indices = [int(n) - 1 for n in choix.split()]  # le joueur tape 1 à 5, la liste va de 0 à 4
    des = relancerDes(des, indices)

print("Nouveaux dés :", des)
import random 
from random import choices

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

faces = range(1, 7)  #  les 6 faces d'un dé
 
 
def somme_de_deux_dés() -> int:
    # on tire 2 dés, on fait la somme
    return sum(choices(faces, k=2))
import random
from constantes import NB_FACES
#Traitement des dés
def lancerUnDe(n):
    """Lance un dé à n faces."""
    return random.randint(1, n)
 
 
def lancerDeDes(nbDes, nbFaces):
    """Lance nbDes dés et renvoie la liste des valeurs."""
    listeDesDes = []  # la liste des dés, pour l'instant vide
    for i in range(nbDes):
        d = lancerUnDe(nbFaces)  # on lance un dé
        listeDesDes.append(d)    # on ajoute ce dé à la liste
    return listeDesDes
 
 
def relancerDes(listeDesDes, indices, nbFaces=NB_FACES):
    """Relance seulement les dés dont l'indice est dans `indices`."""
    for i in indices:
        listeDesDes[i] = lancerUnDe(nbFaces)
    return listeDesDes
from collections import Counter
from constantes import SCORES
#Traitement des mains et du score

def reconnaitreMain(listeDesDes):
    """Renvoie le nom de la main """
    compte = Counter(listeDesDes)                        # ex : [3,6,1,6,2] -> {6:2, 3:1, 1:1, 2:1}
    occurrences = sorted(compte.values(), reverse=True)  # ex : [2, 1, 1, 1]
 
    """Vérifier si est nous avons une suite, 5 valeurs différentes qui se suivent"""
    valeurs = sorted(set(listeDesDes)) # on trie et on renvoie le nb de chiffres uniques dans notre liste
    estSuite = len(valeurs) == 5 and valeurs[-1] - valeurs[0] == 4 
    #len(valeurs) == 5 vérifie si y'a pas de doublon, si on a 5, on a bel et bien 5 dés avec 5 chiffres différents
    #valeurs[-1] - valeurs[0] == 4 vérifie si l'écart entre le plus grand dé et le plus petit est de 4 (ex: 5-1=4 ou 6-2=4)
    #comme len(valeurs) elimine les doublons et l'écart est de 4, c'est bien une suite car le chemin est forcément des nombres consécutifs

 
    if occurrences[0] == 5:
        return "Yams"
    if occurrences[0] == 4:
        return "Carré"
    if occurrences == [3, 2]:
        return "Full"
    if estSuite:
        return "Suite"
    if occurrences[0] == 3:
        return "Brelan"
    if occurrences[:2] == [2, 2]:
        return "Double paire"
    if occurrences[0] == 2:
        return "Paire"
    return "Carte haute"
 
 
def calculerScore(listeDesDes):
    """Renvoie (nom de la main, nombre de points)."""
    main = reconnaitreMain(listeDesDes)
    return main, SCORES[main]
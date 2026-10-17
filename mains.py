from collections import Counter
from constantes import SCORES
#Traitement des mains et du score

def reconnaitreMain(listeDesDes):
    """Renvoie le nom de la main (Paire, Brelan, Full...)."""
    compte = Counter(listeDesDes)                        # ex : [3,6,1,6,2] -> {6:2, 3:1, 1:1, 2:1}
    occurrences = sorted(compte.values(), reverse=True)  # ex : [2, 1, 1, 1]
    valeurs = sorted(set(listeDesDes))
 
    # une suite = 5 valeurs différentes qui se suivent
    estSuite = len(valeurs) == 5 and valeurs[-1] - valeurs[0] == 4
 
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
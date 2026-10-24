#Ici, nous créons nos personnages 
from constantes import VALEUR_MAX_MORALE_PERSO
from constantes import VALEUR_MAX_MORALE_GOD

class Personnage():
    def __init__(self, nom: str, morale_initiale: int):
        self.nom = nom 
        self.morale = morale_initiale  

    @property
    def morale(self):
        return self._morale 

    @morale.setter
    def morale(self, valeur):
        self._morale = max(0, min(VALEUR_MAX_MORALE_PERSO, valeur))


class Dieu(Personnage): 
    def __init__(self, nom, morale, force: int):
        super().__init__(nom, morale)
        self.force = force 
    
    @property
    def morale(self):
        return self._morale 

    @morale.setter
    def morale(self, valeur):
        self._morale = max(0, min(VALEUR_MAX_MORALE_GOD, valeur))





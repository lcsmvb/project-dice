#Ici, nous créons nos personnages 

class Personnage():
    def __init__(self, nom: str, pv: int):
        self.nom = nom 
        self._pv = pv 

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, valeur):
        self._pv = max(0, valeur)



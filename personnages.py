#Ici, nous créons nos personnages 

class Personnage():
    def __init__(self, nom: str, morale: int):
        self.nom = nom 
        self._morale = morale 

    @property
    def morale(self):
        return self._morale 

    @morale.setter
    def morale(self, valeur):
        self._morale = max(0, min(1000, valeur))

Protagoniste = Personnage("Protagoniste", 100)

class Dieu(Personnage): 
    def __init__(self, nom, morale, force: int):
        super().__init__(nom, morale)
        self._force = force 

    @property
    def force(self):
        return self._force 
    
    @force.setter
    def force(self, valeur):
        self._force = max(0, min(1000, valeur))

Hermes = Dieu("Hermès", 100, 620)




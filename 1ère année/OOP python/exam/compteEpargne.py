from compte import Compte
class CompteEpargne(Compte):
    interet=""
    def __init__(self,numero , propriertaire, solde, dateOuverture,interet):
        Compte.__init__(self,numero , propriertaire, solde, dateOuverture)
        self.interet=interet
    
    def getInteret(self):
        return self.interet
    def __str__(self):
        return Compte.__str__(self)+" Interet :"+self.interet

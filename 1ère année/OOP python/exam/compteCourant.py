from compte import Compte

class CompteCourant(Compte):
    montantDecouvertAutorise=0.
    def __init__(self, numero , propriertaire, solde, dateOuverture, montantDecouvertAutorise):
        Compte.__init__(self,numero , propriertaire, solde, dateOuverture)
        self.montantDecouvertAutorise=montantDecouvertAutorise
    
    def getMantant(self):
        return self.montantDecouvertAutorise
    
    def __str__(self) :
        return Compte.__str__(self)+ " Montant Decouvert Autorise :"+ str(self.montantDecouvertAutorise)
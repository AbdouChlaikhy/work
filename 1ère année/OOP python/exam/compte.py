import datetime 
class Compte:
    numero=0
    proprietaire=""
    solde=0.0
    dateOuverture=datetime.datetime.date.__new__

    def __init__(self,numero , propriertaire, solde, dateOuverture):
        self.numero=numero
        self.proprietaire=propriertaire
        self.solde=solde
        self.dateOuverture=dateOuverture
        
    def getNumero(self):
        return self.numero
    def getProprietaire(self):
        return self.proprietaire
    def getSolde(self):
        return self.solde
    def getDateOuverture(self):
        return self.dateOuverture
    
    def __str__(self):
        return "Numero :"+str(self.numero)+" Proprietaire :"+self.proprietaire +" solde :"+ str(self.solde)+ " dateOuverture :"+self.dateOuverture.strftime("%x")
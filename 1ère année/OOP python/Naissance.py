





class DateNaissance:
    def __init__(self,jour,mois,annee):
        self.__jour=jour
        self.__mois=mois
        self.__annee=annee
    def __str__(self):
        return str(self.__jour) +"/"+str(self.__mois)+"/"+str(self.__annee)
   
    
class Personne:
    
    def __init__(self,nom,prenom,DateN):
        
        self.nom=nom
        self.prenom=prenom
        self.DateN=DateN
    def affiche(self):
        print(" Nom : ", self.nom ,"\n","Prenom :", self.prenom,"\n Date De Naissance: ",self.DateN)
class Employe(Personne):
    def __init__(self,n,p,d,S):
        Personne.__init__(self,n,p,d)
        self.salaire=S
    def affiche(self):
        Personne.affiche(self)
        print("Salaires: ",self.salaire,"DH")
class Chef(Employe):
    def __init__(self, n, p, d, S,service):
        super().__init__(n, p, d, S)
        self.service=service
    def affiche(self):
        return super().affiche()






B=Personne("Chlaikhy","Abderrahmane",DateNaissance(27,12,1999))
B.affiche()

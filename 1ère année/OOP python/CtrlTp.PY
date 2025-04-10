from abc import ABC,abstractclassmethod
from mimetypes import init
from re import A




class Client :
    def __init__(self,NumCl,NomCl):
        self.NumCl=NumCl
        self.NomCl=NomCl
    def getNumCl(self):
        return self.NomCl
    def setNumCl(self,NumCl):
        self.NumCl=NumCl
    def getNomCl(self):
        return self.NomCl
    def setNomCl(self,NomCl):
        self.NomCl=NomCl
    def __str__(self):
        return "\nNumero du Client : "+ str(self.NumCl)+ " \nNom du Client : "+ self.NomCl
class Compte(ABC) :   
    
    def __init__(self,NumCT,Solde,PropCT):
        self.NumCT=NumCT
        self.Solde=Solde
        self.PropCT=PropCT
    def __str__(self):
        return "Numero Du Compte : "+str(self.NumCT)+"\n Propriétaire : "+self.PropCT.__str__()+"\n Solde : "+str(self.Solde)
    def Depot(self,Somme):
        self.Solde+=Somme
    def retrait(self,Somme):
        if Somme<self.Solde:
            self.Solde-=Somme
        else :
            print("Votre Solde Est Insuffisant")
class CompteCourant(Compte):
    def __init__(self, NumCT, Solde, PropCT,Decouvert):
        super().__init__(NumCT, Solde, PropCT)
        self.Decouvert=Decouvert
    def __str__(self):
        return super().__str__()+"\n decouvert : "+ str(self.Decouvert)
    def retrait(self, Somme):
        if (self.Solde+ self.Decouvert)>=Somme:
            self.Solde=(self.Solde+self.Decouvert)-Somme
            if self.Solde<0:
                self.Decouvert+=self.Solde
        else:
            print("Solde insuffisant")
class Banque:
    
    def __init__(self,NumCT,Solde,PropCT):
        self.NumCT=NumCT
        self.Solde=Solde
        self.PropCT=PropCT
        self.T=[]
    def Ajouter(self,a):
        self.T.append(a)
    def Afficher(self):
        for i in self.T:
            print(i)
    def Supprimer(self,b):
        for i in range(len(self.T)):
            if b.getNumCl()==self.T[i].PropCT.getNumCl:
                del self.T[i]
        
    



A=Compte(12345678,3000,Client(123,"jjjj"))
Banque.Ajouter(A,A)
Banque.Afficher()

 


























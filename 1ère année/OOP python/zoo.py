
from abc import ABC,abstractclassmethod

class Animal(ABC):
    def __init__(self,nom,race,age,poids):
        self.Nom=nom
        self.Race=race
        self.setAge(age)
        self.setPoids(poids)
    def getNom(self):
        return (self.Nom)
    def getRace(self):
        return (self.Race)
    def getAge(self):
        return (self.Age)
    def getPoids(self):
        return (self.Poids)
    def setNom(self,nom):
        self.Nom=nom
    def setRace(self,race):
        self.Race=race
    def setAge(self,age):
        if age>0:
            self.Age=age
        else:
            print("age invalid")
    def setPoids(self,poids):
        if poids>0:
            self.Age=poids
        else:
            print("poids invalid")
        self.Poids=poids
    def __str__(self):
        return "Nom: "+ self.Nom + "Race: "+ self.Race + "Age : "+ str(self.Age) + "Poids: "+str(self.Poids)
    @abstractclassmethod
    def Deplacer(self):
        pass 
class chien(Animal) :
    def __init__(self,nom,age,poids):
        Animal.__init__(self,nom,"Chien",age,poids)
        
    def Deplacer(self):
        print("Marche Sur quatres Pâttes")

class oiseau(Animal) :
    def __init__(self,nom,age,poids):
        Animal.__init__(nom,"Oiseau",age,poids)
    def Deplacer(self):
        print("Se déplace en nageant")    
        
class poisson (Animal) :
    def __init__(self,nom,age,poids):
        Animal.__init__(nom,"Poisson",age,poids)
    def Deplacer(self):
        print("Se Deplace en volant")
        
class Zoo:
    def __init__(self):
        self.T=[]
    def Ajouter(self,a):
        self.T.append(a)
        

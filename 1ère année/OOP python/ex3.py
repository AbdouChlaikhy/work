from calendar import c
from re import S
from tkinter import N


class Filière:
    nbrfiliere=0
    def __init__(self,code,nom,secteur):
        self.__code=code
        self.__nom=nom
        self.__secteur=secteur 
        Filière.nbrfiliere+=1
    def getCode(self):
        return(self.__code)
    def getNom(self):
        return(self.__nom)
    def getSec(self):
        return(self.__secteur)
    def setCode(self,code):
        self.__code=code
    def setNom(self,nom):
        self.__nom=nom
    def setSec(self,secteur):
        self.__secteur=secteur
    def __str__(self):
        return("code="+self.__code+"/"+"nom:"+self.__nom+"/"+"secteur:"+self.__secteur)
print(Filière.nbrfiliere)
f1=Filière("101Dig","Dev","digital")
print(Filière.nbrfiliere)
print()

import csv
import json






class Personne :
    def __init__(self,n,p,a):
        self.nom=n
        self.prenom=p
        self.age=a
    def getNom(self):
        return self.nom
    def getPrenom(self):
        return self.prenom
    def getAge(self):
        return self.age
    def setNom(self,n):
        self.nom=n
    def setPrenom(self,p):
        self.prenom=p
    def setAge(self,a):
        self.age=a
    def __str__(self):
        return "Nom : "+self.nom+" Prenom : "+self.prenom+"Age : "+str(self.age)
class Groupe:
    def __init__(self):
        self.T=[]
    def ajouter(self,P):
        self.T.append(P)
    def afficher(self):
        for i in self.T:
            print(i)
            print("*****************")
    def savetxt(self):
        F=open("serie9//Personne.txt","w")
        for i in self.T:
            F.write(i.__str__()+ "\n")
            
        F.close()
    def Liretxt(self):
        F=open("serie9//Personne.txt","r")
        for i in F :
            print(i)
            
        F.close()
    def saveCSV(self):
        F=open("serie9//P2.csv","w")
        a=csv.writer(F,delimiter=";")
        for i in self.T:
            P=[i.nom,i.prenom,i.age] 
            a.writerow(P)

        F.close()     
    def LireCSV(self):
        F=open("serie9//P2.csv","r")
        a=csv.reader(F)
        for i in self.T:
            print(i)
    def saveJson(self):
        F=open("serie9//P3.json","r")
        w=json.loads(F.read(self.T))
        print(w)










a=Personne("zouhair","hamza",25)

b=Groupe()

b.ajouter(a)

b.savetxt()


b.saveCSV()
b.LireCSV()



























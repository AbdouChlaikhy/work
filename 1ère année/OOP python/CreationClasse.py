class Stagiaire :
    def __init__(self,n,n1,n2):
        self.nom = n
        self.Note1 = n1
        self.Note2 = n2
    def affiche(self):
        print(self.nom,"\n",self.Note1,"\n",self.Note2)
    def moyen(n1,n2):
        M=(n1+n2)/2
        return M
S1=Stagiaire("Abdou",15,17)

print("S1\n")
S1.affiche()


n="Abdou"
n1=18
n2=20
S2=Stagiaire(n,n1,n2)
print("S1 \n")
S2.affiche()
print("Moyen de Abdou S2")
S2.moyen(n1,n2)


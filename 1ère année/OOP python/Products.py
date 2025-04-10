




class PrixException(Exception):
    pass

class Produit:
    Pa=0
    Pv=0
    def __init__(self,code,libelle,Pv,Pa):
        self.code=code
        self.libelle=libelle
        self.Pv=Pv
        self.setPa(Pa)
        
        
    def gain(self):
        return self.Pv-self.Pa
    def __str__(self):
        return "code: "+str(self.code)+"\nlibelle : "+self.libelle+"\nPrix Achat : "+str(self.Pa)+"\Prix Vente : "+str(self.Pv)
    
    def setPa(self,A):
        if (self.Pv<A):
            raise PrixException()
        else :
            self.Pa=A

    def setPv(self,v):
        if (self.Pa>v):
           raise PrixException() 
        else :
            self.Pv=v

try:
    
    P1=Produit(1234,"zyad",60,40)
    print(P1)
    P1.setPv(float(input("Entrez le prix dE VENTE : ")))
    print(P1)
except PrixException:
    print("prix de vente doit etre sup au prix d'achat ")
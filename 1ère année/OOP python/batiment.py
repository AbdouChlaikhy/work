class Batiment:
    
    def __init__(self,adresse):
        self.adresse=adresse
    def getadr(self):
        return self.adresse
    def setadr(self,adr):
        self.adresse=adr
    def __str__(self):
        return "adresse: "+(self.adresse)
class Maison(Batiment):
    def __init__(self,adresse,nbPiéces):
        Batiment.__init__(self,adresse)
        self.nbPiéces=nbPiéces
    def getnbP(self):
        return self.nbPiéces
    def setnb(self,a):
        self.nbPiéces=a
    def __str__(self):
        return Batiment.__str__(self)+", nombre de piéces: "+str(self.nbPiéces)
class Immeuble(Batiment):
    def __init__(self,adresse,nbAppart):
        Batiment.__init__(self,adresse)
        self.nbAppart=nbAppart
    def getnbA(self):
        return self.nbAppart
    def setnba(self,a):
        self.nbAppart=a
    def __str__(self):
        return "adresse: "+(self.adresse)+", avec nombre d'Appartement: "+str(self.nbAppart)

m1=Maison("derb Seltan",3)
print(m1)
I1=Immeuble("Sdi Maarouf",17)
print(I1)

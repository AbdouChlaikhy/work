class VeloElec:
    def __init__(self,a,k):
        self.Autonomie=a
        self.Kilometrage=k
    def Rouler(self,d):
        self.Kilometrage+=d
        return self.Kilometrage
    def Charger(self,m):
        self.Autonomie=



    def __str__(self):
        return "Autonomie: "+str(self.Autonomie)+"Kilometrage :"+str(self.Kilometrage)
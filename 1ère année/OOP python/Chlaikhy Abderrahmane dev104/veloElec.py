
from appareil import Appareil








class VeloElec(Appareil):
    def __init__(self,ref,pu,po,pr,a,k):
        Appareil.__init__(ref,pu,po,pr)
        self.Autonomie=a
        self.Kilometrage=k
    def Rouler(self,d):
        self.Kilometrage+=d
        return self.Kilometrage
    def Charger(self,m):
        self.Autonomie+=m*10/60
    def __str__(self):
        return Appareil.__str__()+"Autonomie: "+str(self.Autonomie)+"Kilometrage :"+str(self.Kilometrage)
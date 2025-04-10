
import re



class Appareil:
    def __init__(self,ref,pui,poids,prix):
        r=re.compile(r"^[A-Z]{2}/[0-9]{3}$") 
        if r.match(ref):
            self.ref=ref
        else:
            raise Exception ()
        self.Puissance=pui
        self.Poids=poids
        self.Prix=prix
    
        
    def __str__(self):
        return "Reference : "+self.ref+"Puissance : "+str(self.Puissance)+" Poids : "+str(self.Poids)+"Prix : "+str(self.Prix)+"Dhs"
    def ClassEneergetique(self):
        if  self.Puissance<300:
            print("Appareil de Class A")
        elif self.Puissance<=1000:
            print("Appareil de Class B")
        else:
            print("Appareil de Class C")
        
        












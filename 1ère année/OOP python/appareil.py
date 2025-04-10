import re


class RefExcept(Exception):
    pass



class Appareil:
    def __init__(self,ref,pui,poids,prix):
        self.setRef(ref)
        self.Puissance=pui
        self.Poids=poids
        self.Prix=prix
    def setRef(self,ref):
        r=re.compile(r"^[A-Z]{2}/[0-9]{3}$")
        if r.match(ref):
            self.ref=ref
        else:
            raise RefExcept ()
    def __str__(self):
        return "Reference : "+self.ref+"Puissance : "+str(self.Puissance)+"Poids : "+str(self.Poids)+"Prix : "+str(self.Prix)+"Dhs"
    def ClassEneergetique(self,P):
        if P>0 and P<300:
            print("Appareil de Class A")
        elif P>=300 and P<=1000:
            print("Appareil de Class B")
        elif P>1000:
            print("Appareil de Class C")
        else :
            print("Puissance Invalid")













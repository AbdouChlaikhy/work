from logging import exception
import re
from unicodedata import name
from weakref import ref 
from abc import ABC,abstractclassmethod
import datetime
class ExpIllegalleMicroPro(Exception):
    pass
class ExpIllegaleReference(Exception):
    pass
class Materiele(ABC):
    def __init__(self,ref="AA00000000",marque="azerty"):
        self.setRef(ref)
        self.Marque=marque
        self.Date=datetime.date.today()
    def getRef(self):
        return self.ref
    def getMarque(self):
        return self.Marque
    def getDate(self):
        return self.Date
    def setMarque(self,marque):
        self.Marque=marque
    def setDate(self,date):
        self.Date=date
    def setRef(self,ref):
        r=re.compile(r"^[A-Z]{2}[0-9]{8}$")
        if r.match(ref):
            self.ref=ref
        else:

            raise ExpIllegaleReference ()
        
        
    def __str__(self):
        return "Référence :"+self.ref+"\nMarque :"+self.Marque+"\nDate d'achat :"+self.Date
class Ordinateur(Materiele):
    def __init__(self, ref="AA00000000", marque="azerty",A="Mic",capROM="ROM",capRAM="RAM"):
        Materiele().__init__(self,ref, marque)
        self.MicType=A
        self.CapROM=capROM
        self.CapRAM=capRAM
    def __str__(self):
        return Materiele.__str__()+"Type du Micro : "+self.MicType+"\nCapacité disk dur: "+self.CapROM+"Capacité RAM :"+self.CapRAM
    def 




     



"""ya weld l9ehba kemlo mn tel 24/03/2022"""











class organisme(ABC):
    def __init__(self,tel="",adresse="",mail=""):
        self.tel=tel
        self.adresse=adresse
        self.mail=mail
    def __str__(self):
        return "telephone : "+self.tel+"\nadresse: "+self.adresse+"\nadresse Mail: "+self.mail
class OrganismeNonLucratif(organisme):
    def __init__(self,A="",B="",C="",Act=""):
        organisme.__init__(self,A,B,C)
        self.activite=Act
    def __str__(self):
        return organisme.__str__+"Activite : "+self.activite

class organismeEntreprise(organisme):
    def __init__(self, tel="", adresse="", mail="",):
        super().__init__(tel, adresse, mail)












def supp(self,A):
    for i in self.T:
        if i.nC==A:
            self.T.remove(i)
            
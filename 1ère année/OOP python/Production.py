from abc import ABC,abstractclassmethod
class composition:
    
    def __init__(self,P,Q):
        
        self.__Produit=P
        self.__Quantite=Q
    @property
    def produit(self):
        return self.__Produit
    @property
    def quantite(self):
        return self.__Quantite
    @produit.setter
    def produit(self,p):
        self.__Produit=p
    @quantite.setter
    def quantite(self,q):
        self.__Quantite=q
class Produit(ABC)
    
    
c=composition('ss',23)
print(c.produit)
c.produit='ee'
print(c.produit)


class Document:
    def __init__(self,num,titre):
        self.num=num
        self.titre=titre
    def getNum(self):
        return self.num
    def gettitre(self):
        return self.titre
    def setNum(self,num):
        self.num=num
    def setTitre (self,titre):
        self.titre=titre
    def __str__(self):
        return str(self.num)+":"+self.titre
class Livre(Document):
    def __init__(self, num, titre,auteur,nbPage):
        super().__init__(num, titre):
        e
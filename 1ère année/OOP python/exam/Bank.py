class Bank:
    def __init__(self):
        self.L=[]
    
    def ajouter(self,cmp):
        self.L.append(cmp)
    def afficher(self):
        for c in self.L:
            print(c)
        

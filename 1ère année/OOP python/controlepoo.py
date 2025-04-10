from abc import ABC, abstractclassmethod


class Client:
    numCli = 1
    nomCli = ""

    def __init__(self, numCli, nomCli):
        self.numCli = numCli
        self.nomCli = nomCli

    def getNumC(self):
        return self.numCli

    def getNomC(self):
        return self.nomCli

    def setNumC(self, numC):
        self.numCli = numC

    def setNomC(self, nomC):
        self.nomCli = nomC

    def __str__(self):
        return "Numéro de Client : "+str(self.numCli)+"\nNom de Client :" + self.nomCli


class Compte (ABC):
    numCompte = 1
    soldeCompte = 0.0
    propCompte = Client(1, "")

    def __init__(self, numCompte, soldeCompte, propCompte):
        self.numCompte = numCompte
        self.soldeCompte = soldeCompte
        self.propCompte = propCompte

    def __str__(self):
        return "Numéro de compte : "+str(self.numCompte)+"\nSolde de compte : "+str(self.soldeCompte)+"\nPropriétaire de compte :  "+self.propCompte.__str__()

    def depot(self, M):
        self.soldeCompte += M

    def retrait(self, M):
        if M <= self.soldeCompte:
            self.soldeCompte -= M
        else:
            print("solde insuffisant")


class CompteCourant (Compte):
    decouvert = 0.0

    def __init__(self, numCompte, soldeCompte, propCompte, decouvert):
        Compte.__init__(self, numCompte, soldeCompte, propCompte)
        self.decouvert = decouvert

    def __str__(self):
        return Compte.__str__(self)+"\nDecouvert : "+str(self.decouvert)

    def retrait(self, M):
        if M <= self.soldeCompte+self.decouvert:
            self.soldeCompte = self.soldeCompte-M
            if self.soldeCompte < 0:
                self.decouvert += self.soldeCompte
        else:
            print("solde insuffisant")


class Banque:
    def __init__(self):
        self.T = []

    def ajouter(self, C):
        self.T.append(C)

    def afficher(self, S):
        for C in self.T:
            if S < C.soldeCompte:
                print(C)

    def afficherListe(self):
        for C in self.T:
            print("¨¨"*60)
            print(C)
        print("¨¨"*60)

    def supprimer(self, Clt):
        j = 0
        for i in range(len(self.T)):
            if Clt.getNumC() == self.T[j].propCompte.getNumC():
                del self.T[j]
                j -= 1
                print("Compte supprimé")
            j += 1

    def depotSolde(self, numC):
        for C in self.T:
            if numC == C.numCompte:
                S = float(input("entrez le montant de depot:"))
                C.depot(S)

    def retraitMontant(self, numCmp):
        for C in self.T:
            if numCmp == C.numCompte:
                M = float(input("entrez le montant de retrait :"))
                C.retrait(M)
                print("opération bien successive")


B1 = Banque()
choix = 0
while choix != 7:
    print("*"*60)
    print("1- Ajouter un compte")
    print("2- Afficher tous les comptes")
    print("3- Afficher les comptes dont le solde est supérieure à un solde saisie")
    print("4- Supprimer un compte")
    print("5- Déposer un solde dans un compte")
    print("6- Retrait")
    print("7- Quitter")
    print("*"*60)
    choix = int(input("saisir votre choix :"))
    if choix == 1:
        numCo = int(input("etrez le numéro de compte : "))
        S = float(input("entrez le solde de client :"))
        NC = int(input("entrez le numéro de client :"))
        nomC = input("entrez le nom de client :")
        decouvert = float(input("entrez le montant de découvert : "))
        C = CompteCourant(numCo, S, Client(NC, nomC), decouvert)
        B1.ajouter(C)
    elif choix == 2:
        B1.afficherListe()
    elif choix == 3:
        B1.afficher(float(input("entrez le solde :")))
    elif choix == 4:
        C1 = Client(int(input("entrez le numéro de client :")),
                    input("entrez le nom de client :"))
        B1.supprimer(C1)
    elif choix == 5:
        numCo = int(input("entrez le numéro de compte : "))
        B1.depotSolde(numCo)
    elif choix == 6:
        numCmp = float(input("entrez le numéro de compte à retraiter :"))
        B1.retraitMontant(numCmp)
    elif choix == 7:
        print("Fin")
    else:
        print("choix invalide")

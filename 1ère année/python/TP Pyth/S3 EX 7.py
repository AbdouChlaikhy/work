A=str(input("Entrez votre nom:"))
B="Martin"
if A==B :
    print("bienvenue Martin")
    C=int(input("Entrez le jour de votre naissance: "))
    D=int(input("Entrez le mois de votre naissance: "))
    if C==3 and D==11:
        print("Joyeux anniversaire Martin")
else :
    print("ERROR:Nom d'utilisateur inconnu.")

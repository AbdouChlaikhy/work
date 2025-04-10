A=int(input("Entrez l'age de votre enfant: "))
if A<6 and A>0:
    print("Votre enfant doit avoir au moins 6ans")
elif A==6 or A==7:
    print('votre enfant appartien à la catégorie"Poussin"')
elif A==8 or A==9:
    print('votre enfant appartien à la catégorie"Pupille"')
elif A==10 or A==11:
    print('votre enfant appartien à la catégorie"Minime"')
elif A>12:
    print('votre enfant appartien à la catégorie"Cadet"')
else:
    print("l'age que vous avez entrez est invalid")

S=0
A=1
while A>0 :
    A=float(input("Entrez le montant du produit: "))
    S=S+A
print("Le montant a payer est : ",S)
B=float(input('Entrez la somme que vous payez: '))
if B<S:
    print("somme insuffisante")
else :
    print('le reste à rendre : ',B-S)

A=float(input("Entrez un nombre"))
B=float(input("Entrez un nombre"))
if (A<0 and B<0) or (A>0 and B>0):
    print("le produit de ces deux nombres est positive")
elif (A>0 and B<0) or (A<0 and B>0):
    print("le produit de ces deux nombres est negatif")
else:
    print("LE produit de ces deux nombres est nul")

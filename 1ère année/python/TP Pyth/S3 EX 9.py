A=float(input("Entrez Le Montant: "))
if A>=2000 and A<=5000:
    print("Montant net =",A-(A*0.01))
elif A>5000:
    print("Montant net =",A-(A*.02))
else :
    print("Montant net =",A)

A=int(input("Entrez un Entier: "))
for i in range (2,A):
    if A%i==0:
        print(A,"n'est pas un nombre premier")
        break
else:
    print(A,"est un nombre premier")
        

import math 
A=int(input("Entrez la valeur de A: "))
B=int(input("Entrez la valeur de B: "))
C=int(input("Entrez la valeur de C: "))
D=B*B-4*A*C
if D>0:
    G=math.sqrt(D)
    X1=(-B-G)/2*A
    X2=(-B+G)/2*A
    print(" cette equation admet deux Solutions \n X1=",X1,"    X2=",X2)
elif D==0:
    X=-B/2*A
    print("cette equation admet une solution \n X=",X)
else :
    print("cette equation na aucune solution dans R")

import math 
A=float(input("Entrez la valeur de A: "))
B=float(input("Entrez la valeur de B: "))
C=float(input("Entrez la valeur de C: "))
D=B*B-4*A*C
if D>0:
    G=math.sqrt(D)
    X1=(-B-G)/2*A
    X2=(-B+G)/2*A
    print(" cette equation admet deux Solutions dans R \n X1=",X1,"    X2=",X2)
elif D==0:
    X=-B/2*A
    print("cette equation admet une solution dans R  \n X=",X)
else :
    G=math.sqrt(-D)
    print("cette equation admet deux Solutions dans C \n X1=",-B/2*A,"+i",G/2*A,"        X2=",-B/2*A,"-i",G/2*A)

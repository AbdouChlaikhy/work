A = int(input("Entrez le premier nombre :"))
B = int(input("Entrez le deuxieme nombre :"))
c = 0
if A<B :
    min = A
else:
    min = B
for i in range(1, min+1):
    if A % i == 0 and B % i == 0 :
        C = i
print("le pgcd de", A, "et", B, "c'est :", C)

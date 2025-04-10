#Ecrire un programme qui permet de remplir un tableau par N entier
#et d'afficher le max avec sa position
T=[]
X=0
N=int(input("Entrez le nombre des elements: "))
for i in range (N):
    T.append(int(input("Entrez un valeur:")))
A=T[0]
for i in range (N):
    if (T[i]>A):
        X=i
        A=T[i]
print('le max est ',A," et sa position est ",X)

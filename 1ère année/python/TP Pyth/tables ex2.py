T=[]
N=int(input("Entrez le nombre des elements"))
for i in range(N):
    T.append(int(input("Entrez une valeur:")))
K=0
X=int(input("Entrez le X dont vous voulez supprimer"))
for i in range(0,N):
    A=2+1
    if T[i]==X:
        del T[i]
print(T)

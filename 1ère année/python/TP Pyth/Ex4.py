
L=[]
T=[]
n=int(input("Entrez le nombre de Personnes que vous voulez enregistrer: "))

for i in range(n):
    dic={}
    num=(input("Entrez le numero de telephone: "))
    nom=(input("Entrez le nom du contact: "))
    
    dic[num]=nom
    L.append(dic)
print(L)
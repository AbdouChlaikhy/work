#ex2 efm
dic={}
L=[]
T=[]
fic={}
n=int(input("Entrez le nombre de Personnes que vous voulez enregistrer: "))

for i in range(n):
    num=int(input("Entrez le numero de telephone: "))
    nom=(input("Entrez le nom du contact: "))
    while len(num)!=4 or num.isnumeric()==False:
        num=int(input("Entrez un numero qui se compose de 10 chiffres: "))
    dic[num]=nom
    L.append(num)




    #print(new_list)
#(    L.append(num)
#    T.append(nom)
#print(dic)
#print(L)

#L.sort()
#L.reverse()


#print(L)
#for i in range (n):
 #   fic[L[i]]=T[i]

#print(fic) )
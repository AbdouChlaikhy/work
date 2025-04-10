#dic={}
#for i in range (2):
    #A=input("Entreee")
    #B=input("entre")
    #dic[A]=B
#print(dic.values())



T=[]
N=int(input("Entrez le nombre de personnes: "))
for i in range(N):
    
    nom = input("Entrez le nom: ")
    
    prenom = input("Entrez le prenom: ")
    
    age = int(input("Entrez votre age: "))
    dic={"nom":nom,"prenom":prenom,"age":age}

    T.append(dic)
val_nom=[dic["nom"]for dic in  T]
val_pre=[dic["prenom"] for dic in T]
val_age=[dic["age"] for dic in T]

#print(val_nom)
#print(val_pre)
#print(val_age)

print("nom | prenom | age")
for i in range(N):
    print(val_nom[i],"|",val_pre[i],"|",val_age[i])
print(T)



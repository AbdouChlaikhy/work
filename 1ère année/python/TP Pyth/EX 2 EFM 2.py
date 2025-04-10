#Ex2 efm
L=[]
n=int(input("Entrez le nombre de perssone"))
for i in range (n):
    dic={}
    num=(input("Entrez le numero de telephone: "))
    nom=(input("Entrez le nom du contact: "))
    while len(num)!=4 or num.isnumeric()==False:
        num=input("Entrez un numero qui se compose de 10 chiffres: ")
    dic[num]=nom
    L.append(dic)
    #new_list = []
 #   while L:
  #      minimum = L[0][num] 
   #     for x in L: 
    #        if x < minimum:
     #          minimum = x
     #     new_list.append(minimum)
      #  L.remove(minimum)
    #print(new_list)
print(dic)
        
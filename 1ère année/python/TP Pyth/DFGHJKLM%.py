A=input("Entrez une chaine : ")
T=[]
for i in A:
    if i not in T:
        print(i,' figure ',A.count(i),"fois dans la chaine")
        T.append(i)
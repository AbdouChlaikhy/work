A=float(input("Entrez Votre Note:"))
if  A>20 or A<0 :
    print("La Note doit etre comprise entre 0-20")
elif  A>=16:
    print("mention TB")
elif  A>=14:
    print("mention B")
elif  A>=12:
    print("mention AB")
elif  A>=10:
    print("passable")
else :
    print("Ajourné")

import csv
t=[]
#la saisie des infos
N=int(input("entrez le nombre de personnes:"))
for i in range(N):
    pr={}
    pr['nom']=input("entrez le nom:")
    pr['prenom']=input("entrez le prenom:")
    pr['age']=int(input("entrez l'age:"))
    t.append(pr)
#affichage
print('Nom \t|Prenom \t|Age')
for i in range(N):
    print(t[i]['nom'],'\t|',t[i]['prenom'],t[i]['age'])
#moyenne dage
s=0
for i in range(N):
    s+=t[i]['age']
print('moyenne d\'age : ',s/N)
#afficher les pers avec l
for i in range(N):
    if t[i]['nom'].startswith('l'):
        print(t[i]['nom'])
#afficher la personne la plus age
#supprimer la personne qui se nomme ali
#modifier lage d une personne(saisir nom), lage doit d etre saisi
#enregistrer dans un fichier les personnes qui ont l'age superieur a 30
#enregistrer dans un fichier
with open('per.csv','wt') as f:
    ecrire=csv.DictWriter(f,delimiter=':',fieldnames=t[0].keys())
    ecrire.writeheader()
for line in t:
    ecrire.writerow(line)

from typing import NewType

data_list=[]
N=int(input("Entrez le nombre de caratere: "))
for i in range(N):
    A = int(input("Entrez le nombre : "))
    data_list.append(A)
new_list = []
while data_list:
    minimum = data_list[0]  
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
    
print(new_list)
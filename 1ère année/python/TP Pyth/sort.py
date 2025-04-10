from typing import NewType

data_list = [-5, -9, 5, -54, 23, -45, 6, 67]
new_list = []

while data_list:
    minimum = data_list[0]  
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
    
print(new_list)
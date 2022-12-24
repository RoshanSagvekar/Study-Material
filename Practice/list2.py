'''
Write a Python program to compute the difference between two lists. 
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
'''

c1=['red','orange','green','blue','white']
c2=["black", "yellow", "green", "blue"]
c3=[]
c4=[]
for i in c1:
    if i not in c2:
        c3.append(i)
print('Color1-Color2:',c3)
for j in c2:
    if j not in c1:
        c4.append(j)
print('Color2-Color1:',c4)

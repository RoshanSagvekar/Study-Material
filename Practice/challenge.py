list1=['absb','hajsj','#hshs']
string=''
for item in list1:
    if item[0]!='#':
        string=string+'#'+item
    else:
        string+=item

print(string)

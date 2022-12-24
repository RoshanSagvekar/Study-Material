print('copy')
a = {1: [11,22,33]}
b = a.copy()
print('a:-', a)
print('b:-', b)

a[1].append(44)
print('After append item to a')
print('a:-', a)
print('b:-', b)
a[2]= [44,55,66]
print('After adding new item to a')
print('a:-', a)
print('b:-', b)
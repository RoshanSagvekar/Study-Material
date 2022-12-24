#W.A.P to print number between 1 to 50 in ascending and descending order.?
'''
print('\nAscending Order')
for i in range(1,51):
    print(i,end=',')

print('\nDescending Order')
for i in range(50,0,-1):
    print(i,end=',')
'''
#W.A.P. to print odd numbers between 1 to 50.?
'''
print('\nOdd Numbers Between 1 to 50')
for num in range(1,51):
    if(num%2==1):
        print(num,end=',')
'''

#W.A.P to print number between 1 to 100 divide by 3 and 7 
'''
print('\nNumber between 1 to 100 divide by 3 & 7')
for num in range(1,101):
    if(num%3==0 and num%7==0):
        print(num,end=',')
'''
#W.A.P to print cube series between 1 to 20 

print('Cube Series between 1 to 20')
for num in range(1,21):
    cube=num**3
    print(num,'x',num,'x',num,'=',cube)


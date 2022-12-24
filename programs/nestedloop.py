#Matrix:-

m1=[[11,12,13],[21,22,23],[31,32,33]]

#for loop
'''
for row in m1:
    for col in row:
        print(col,end='\t')
    print()
'''
'''
    Nested loop is used to represent the data in tabular format like 
    * * *
    * * *
    * * *
'''
#Pattern-1
'''
i=1             #row
while i<=3:
    j=1         #column
    while j<=3:
        print('*',end=' ')
        j+=1
    print()
    i+=1
'''
#Dry run table for above program
'''
i   i<=3       j       j<=3        print(*)    j++    i++
1   1<=3(T)    1       1<=3(T)         *        2
1   1<=3(T)    2       1<=2(T)         *        3
1   1<=3(T)    3       1<=3(T)         *        4
1   1<=3(T)    4       1<=4(F)                          2
'''

#Pattern-1 using for loop
'''
for i in range(1,4):
    for j in range(1,4):
        print('*',end=' ')
    print()
'''

#Pattern 2
'''
    1 2 3
    1 2 3
    1 2 3

for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()
''' 
#Pattern 3
'''
1 1 1
2 2 2
3 3 3

for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print()
'''

#Pattern 4
'''
    2 3 4
    3 4 5
    4 5 6

for i in range(1,4):
    for j in range(1,4):
        print(i+j,end=' ')
    print()
'''

#Pattern-5
'''
    *          (1,1)
    * *        (2,1)(2,2)
    * * *      (3,1)(3,2)(3,2)

for i in range(1,4):
    for j in range(1,4):
        if(i>=j):
            print('*',end=' ')
    print()

for i in range(1,4):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
'''
#Pattern-6
'''
    * * *
    * *
    *

for i in range(1,4):
    for j in range(1,5-i):
        print('*',end=' ')
    print()

for i in range(1,4):
    for j in range(3,i-1,-1):
        print('*',end=' ')
    print()

for i in range(1,4):
    for j in range(4,i,-1):
        print('*',end=' ')
    print()

for i in range(4,1,-1):
    for j in range(1,i):
        print('*',end=' ')
    print()

for i in range(1,4):
    for j in range(1,4):
        if(i<=j):
            print('*',end=' ')
    print()
'''
#Pattern-7
'''
        *                (1,3)
      * *           (2,2)(2,3)
    * * *      (3,1)(3,2)(3,3)


for i in range(1,4):
    for j in range(1,4):
        if(j <=3-i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()

n=3     #total no.of rows
for i in range(1,n+1):
    for sp in range(i,n):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()
'''

#Pattern-8
'''
* * * *  sp=0   range(1,1)  star 4->(1,n+1)
  * * *  sp=1   range(1,2)  star 3->(2,n+1)
    * *  sp=2   range(1,3)  star 2->(3,n+1)
      *  sp=3   range(1,4)  star 1->(4,n+1)

n=4
for i in range(1,n+1):
    for sp in range(1,i):
        print(' ',end=' ')
    for j in range(i,n+1):
        print('*',end=' ')
    print()

'''
#Pattern-9
'''
1
1 0
1 0 1
1 0 1 0

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j%2,end=' ')
    print('')
'''
#Pattern-10
'''
    *       sp=3   range(1,4)
   * *      sp=2   range(1,3)
  * * *     sp=1   range(1,2)
 * * * *    sp=0   range(1,1)

n=4
for i in range(1,n+1):
    for sp in range(i,n):
        print(' ', end='')
    for j in range(1,i+1):
        print("* ", end='')
    print()

'''
#Pattern-11
'''
        1   sp=3    range(1,4)
      1 2   sp=2    range(1,3)
    1 2 3   sp=1    range(1,2)
  1 2 3 4   sp=0    range(1,1)

n=4
for i in range(1,n+1):
    for sp in range(i,n):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
#pattern-12
'''
 4 3 2 1 
 3 2 1
 2 1
 1

n=4
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print(j-i,end=' ')
    print() 

'''
#pattern-13
''' 
1
0 1
0 1 0
1 0 1 0

1
2 3
4 5 6
7 8 9 10

n=4
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a%2,end=' ')
        a+=1
    print('')
'''
#pattern-14
'''
1
0 1
1 0 1
0 1 0 1 

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i+j+1)%2,end=' ')
    print('')
'''
#Write a program to check the given no is strong no. or not.
#"Strong number is a number which is equal to summation of each 
# digits is equal to that number."
'''
num=int(input('Enter number='))
temp=num
sum1=0
while num>0:
    digit=num%10       #fetch the digit from number
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum1=sum1+fact
    num=num//10
print('Summation of factorial is',sum1)
if temp==sum1:
    print('The Number is Strong.')
else:
    print('The Number is not Strong.')

n = int(input("Enter a Number : "))
s = 0
digits = len(str(n))
num = n
for i in range(0,digits):
    a = n % 10
    f = 1
    for j in range(1,a+1):
        f = f * j
    s = s + f
    n = n // 10
if num == s :
    print(f"{num} is a Strong Number")
else :
    print(f"{num} is not a Strong Number")
'''


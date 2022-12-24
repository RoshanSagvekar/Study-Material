'''
. Write a program to make a menu-driven program in python using simple if-else
statements for the following operations:
1. Square of Number
2. Cube of Number
3. Nth Power of number
4. Exit
'''
print("-----------------------")
print('1.Square of Number')
print('2.Cube of Number')
print('3.Nth Power of Number')
print('-----------------------')
choice  = int(input('select your Shape:'))

if choice==1:
    num=float(input('Enter a Number='))
    square=num**2
    print('Square of',num,':',square)
elif choice==2:
    num=float(input('Enter a Number='))
    cube=num**3
    print('Cube of',num,':',cube)
elif choice==3:
    num=float(input('Enter a Number='))
    power=int(input('Enter power of number='))
    res=num**power
    print(power,'th Power of',num,':',res)
else:
    print('Your Choice is Invalid...:(\n\tPlease Select Right Choice')
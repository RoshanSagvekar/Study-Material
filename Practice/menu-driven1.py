'''Writer a program to make a menu-driven program in python using simple if-else
statements for the following operations:
1. Area of Circle
2. Area of Rectangle
3. Area of square
4. Exit

'''

print("-----------------------")
print('1.Area of Circle')
print('2.Area of Square')
print('3.Area of Rectangle')
print('----------------------')
choice  = int(input('Select your Shape:'))

if choice ==1:
    radius = float(input('Enter the Radius of Circle:- '))
    area = 3.14 * radius ** 2
    print('Area of Circle is ',area)
elif choice ==2:  # side of square --> side ** 2
    side = int(input('Enter the side of Square '))
    area = side ** 2
    print('Area of Square is ',area)
elif choice ==3:  # length and breath   --> length * breath.
    len = float(input('Enter the Length of Rectangle:- '))
    bre = float(input('Enter the breath of Rectangle:- '))
    area = len * bre
    print('Area of Rectangle is ',area)
else:
    print('Your Choice is Invalid...:(\n\tPlease Select Right Choice')
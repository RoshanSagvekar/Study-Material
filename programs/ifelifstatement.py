#WAP to check entered number is Zero or Negative or Positive
num=int(input('Enter a Number='))

if num>0:
    print('Entered Number is Positive. \nnum:-',num)
elif num<0:
    print('Entered number is Negative. \nnum:-',num)
else:
    print('Entered number is Zero')
print('Program execution is completed.')
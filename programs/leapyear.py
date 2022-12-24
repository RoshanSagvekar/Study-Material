#Use conditional statement to check if a year is a leap year or not.

year=int(input('Enter year to check it is leap or not='))
if (year%400==0) and (year%100==0):
    print(year,' is a leap year.')
elif (year%100!=0) and (year % 4 ==0):
    print(year,' is a leap year.')
else:
    print(year,' is not leap year.')
# The task you have to perform is “Your Age In 2090”. This task consists of a total of 10 points to evaluate your performance.

# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable.
# Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:


 
# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

current_year=2022
age_year=int(input('Enter Your Age or Year of Birth:'))
if len(str(age_year))==4:
    if age_year>current_year:
        print('Oops..! You are not yet Born.')
    elif age_year<=current_year and age_year>1921:
        print('You wil turn 100 in the year',age_year+100,'.')
    elif age_year<=1921:
        print('You are probably ghost.')
elif len(str(age_year))==2 or len(str(age_year))==1:
    if age_year>0:
        print('You wil turn 100 in the year',(100-age_year)+current_year,'.')
    else:
        print('Please Enter Valid Age...!')
else:
    print('Please Enter Valid Age or Year of Birth...')
print('Do you want to know your age in particular year?Type yes if want')
choice=input('Enter Your Choice:')
if choice.lower()=='yes':
    birthyear= int(input('Enter Your Year of Birth:'))
    year=int(input('Enter Particular Year: '))
    if len(str(birthyear))==4 and len(str(year))==4:
        if year>birthyear:
            age=year-birthyear
            print(f'Your age in the {year} will be {age} years.')
            print('THANK YOU...!')
        elif year==birthyear:
            print('You ar just born')
        else:
            print('Oops,You entered wrong birth year or particular year.')
    else:
        print('Please Enter Valid Inputs.')
else:
    print('THANK YOU...!')
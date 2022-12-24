#Write a program to Accept marks 0f 5 subject each subject out 100 and Display Each 
#subject marks, Total Marks and Percentage.

print('Enter marks of subject out of 100')
s1=int(input('Subject-1='))
s2=int(input('Subject-2='))
s3=int(input('Subject-3='))
s4=int(input('Subject-4='))
s5=int(input('Subject-5='))
total=s1+s2+s3+s4+s5
per=total/500*100
print('\nMarks of Subject')
print('Subject-1=',s1,'\nSubject-2=',s2,'\nSubject-3=',s3,'\nSubject-4=',s4,'\nSubject-5=',s5,)
print('Total Marks=',total,'\nPercentage=',per,'%')

if per>=80:
    print('\tCongratulation,You got A+ Grade.')
elif per>=70 and per<=79:
    print('\tCongratulation,You got A Grade.')
elif per>=60 and per<=69:
    print('\tCongratulation,You got B Grade.')
elif per>=50 and per<=59:
    print('\tCongratulation,You got C Grade.')
elif per>=40 and per<=49:
    print('\tCongratulation,You got D Grade.')
else:
    print('\tSorry,You are Fail.\n\tBetter Luck Next Time.')


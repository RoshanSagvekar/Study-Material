'''Input - students percentage
    Output - grade
    Conditions -  percentage >= 60  -  B grade
                  percentage >= 70   - A grade
                  percentage >= 80 - A+ grade
                  else - C  grade'''


per=int(input('Please Enter Your Percentage:-'))
if(per>=60 and per<=70):
    print('Congrats!You got \'B\' Grade.')
elif(per>=70 and per<=80):
    print('Congrats!You got \'A\' Grade.')
elif(per>=80):
    print('Congrats!You got \'A+\' Grade.')
else:
    print('Sorry!You got \'C\' Grade.')

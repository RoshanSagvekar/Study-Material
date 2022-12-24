'''Calculate the bike rent for given usage of vehicle.
for Bike the rent is 100 rs per Hr for 0-3Hrs.  and for 3-5 Hrs the rent is 200 Rs per hour.
for scooty, the rent is 75 Rs per hr for 0-3 hrs. from 3-5 hrs the rent is 150 Rs per hr. 	'''


vehicle=input('Which vehicle do you want Bike or Scooty?\n')
if(vehicle=='Bike' or vehicle=='bike'):
    hrs=int(input('How many hours do you want the vehicle?\n'))
    if(0<hrs<=3):
        rent=hrs*100
        print('rent=',rent,'Rupees')
    elif(3<hrs<=5):
        rent=hrs*200
        print('rent=',rent,'Rupees')
    else:
        print('We do not have service for more than 5 hours.')
elif(vehicle=='Scooty' or vehicle=='scooty'):
    hrs=int(input('How many hours do you want the vehicle?\n'))
    if(0<hrs<=3):
        rent=hrs*75
        print('rent=',rent,'Rupees')
    elif(3<hrs<=5):
        rent=hrs*150
        print('rent=',rent,'Rupees')
    else:
        print('We do not have service for more than 5 hours.')
else:
    print('Please Enter proper vehicle')

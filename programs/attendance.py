'''' A student will not be allowed to sit in exam if his/her attendence is less than 75%.
	Take following input from user
        -Number of classes held
        -Number of classes attended.
        -And print percentage of class attended
        -Is student is allowed to sit in exam or not. '''

n1=int(input('Please Enter total number of held classes='))
n2=int(input('Please Enter number of attended classes= '))
per=n2/n1*100
print('Your attendance is',per,'.')
if(per>75):
    print('Congratulation,You are allowed to sit in exam! :)')
else:
    print('Sorry,You are not allowed to sit in exam! :(')

    
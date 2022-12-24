'''
2. Write a functions in python to perform following operation 2 numbers 
    I. Addition
    II. Subtraction,  
    III. Multiplication,  
    IV. Division
    V nth Power of Number 
e.g
    print (cal_power(5,3) );
'''

def cal_add(n1,n2):
    sum=n1+n2
    print('Addition:',sum)
def cal_sub(n1,n2):
    sub=n1-n2
    print('Subtraction:',sub)
def cal_multi(n1,n2):
    multi=n1*n2
    print('Multiplication:',multi)
def cal_div(n1,n2):
    div=n1/n2
    print('Division:',div)
def cal_power(n1,n2):
    power=n1**n2
    print('Power:',power)

cal_add(45,65)
cal_sub(100,54)
cal_multi(45,5)
cal_div(100,5)
cal_power(12,2)




#WAP to print fibonacci using for loop (0,1 1,2,3,5,8,11,19....)

# num=int(input('Enter limit for fibonnaci Series='))
# n1=0
# n2=1
# nterm=0
# if(num<0):
#     print('The fibonacci series for 0 is',n1)
# elif num<0:
#     print('Please enter a positive number.')
# else:
#     print(num,'terms of fibonacci series are')
#     print(n1,',',n2,end=',')
#     for i in range(2,num):
#         nterm=n1+n2
#         print(nterm,end=',')
#         n1=n2
#         n2=nterm


num=int(input('How many terms you want to print of fibonacci series?'))
a, b = 0, 1
print(num,'terms of fibonacci series are:')
for i in range(0,num):
    print(a)
    a, b = b ,a+b


#Fibonacci Generator
# def fib(num):
#     a, b = 0, 1
#     print(num,'terms of fibonacci series are:')
#     for i in range(0,num):
#         yield "{}: {}".format(i+1,a)
#         a, b = b ,a+b

# terms=int(input('How many terms you want to print of fibonacci series?'))
# for item in fib(terms):
#     print(item)
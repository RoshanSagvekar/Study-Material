#Write a recursive function to calculate the factorial of given Number.

def fact(num):
    if num>1:
        return num * fact(num-1)
    elif num==1:
        return 1
    else:
        return 0

n=int(input('Enter a Number='))
print('Factorial of',n,':',fact(n))

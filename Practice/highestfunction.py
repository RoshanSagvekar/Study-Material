#3.	Create a function using Variable Number of Argument which return the highest arguments value of it.

def highest(*n):
    ans=n[0]
    for i in n:
        if i>ans:
            ans=i
    return ans

print('Highest Value:',highest(5,42,12,32,1))
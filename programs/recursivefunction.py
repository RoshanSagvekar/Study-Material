#What is Recursion?
'''
    The recursion is the process of defining something in itself.
'''
#What is Recursive function?
'''
    In python generally we can call any function from outside that function

    But it is even possible python can call itself i.e
    we can call any function from the same function is 
    known as recursive function.

    It is also know as self calling.
'''
""" 
def sayHi(cnt):
    if cnt>0:
        print('Hi!',cnt)
        return sayHi(cnt-1)
    else:
        return 'abc' 
print(sayHi(5))
"""
def addi(n):
    if n>0:
        return n + addi(n-1)
    else:
        return 0
    
ans=addi(4)
print('Addition:',ans)

# addi(4)                                   1st calling 3
# return 3 +addi(2)                         2nd calling 2
# return 3 + return 2 + addi(1)             3rd calling 1
# return 3 + return 2 + return 1 + addi(0)  4th calling 0
# 3 + 2 + 1 + 0



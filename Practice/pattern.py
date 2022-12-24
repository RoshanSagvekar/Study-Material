#Pattern-1
'''
   *        lsp=3   range(1,4)  star 1-->(4,5)
  ***       lsp=2   range(1,3)  star 3-->(3,6)
 *****      lsp=1   range(1,2)  star 5-->(2,7)
*******     lsp=0   range(1,1)  star 7-->(1,8)

n=4
for i in range(1,n+1):
    for sp in range(1,(n-i)+1):
        print(' ',end='')
    for j in range(1,2*i)
        print('*',end='')
    print()
'''
#Pattern-2
'''
   1
  123
 12345
1234567

n=4
for i in range(1,n+1):
    a=0
    for sp in range(1,(n-i)+1):
        print(' ',end='')
    for j in range(1,2*i):
        a+=1
        print(a,end='')
    print()
'''
#Pattern-3
'''
1	
1 2	
1 2 3	
1 2 3 4

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''

#Pattern-4
'''
1
2 2
3 3 3
4 4 4 4

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
'''
#Pattern-5
'''
1
2 3
3 4 5
4 5 6 7

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i+j-1,end=' ')
    print()
'''

# Pattern-6
''' 
1 1 1 1 1   (1,1)(1,2)(1,3)(1,4)(1,5)
2 2 2 2     (2,1)(2,2)(2,3)(2,4)
3 3 3       (3,1)(3,2)(3,3)
4 4         (4,1)(4,2)
5           (5,1)

n=7
for i in range(1,n):
    for j in range(1,n-i):
        print(i,end=' ')
    print()
 
n=5
b=0
for i in range(n,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end=' ')
    print()
'''
# Pattern-7
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

n=7
for i in range(1,n):
    for j in range(1,n-i):
        print(n-i-1,end=' ')
    print()

'''
# mathematical formula for encryption process x=(c+n)%26
# where x is encode character
# c is actual character
# n is number of position

def cipher(text,shift):
    encrypt_text=''
    for i in text:
        if i.isupper():
            i_unicode=ord(i)
            i_index=ord(i)-ord('A')
            new_index=(i_index+shift)%26
            new_unicode=new_index+ord('A')
            new_char=chr(new_unicode)
            encrypt_text=encrypt_text+new_char
        elif i.islower():
            i_unicode=ord(i)
            i_index=ord(i)-ord('a')
            new_index=(i_index+shift)%26
            new_unicode=new_index+ord('a')
            new_char=chr(new_unicode)
            encrypt_text=encrypt_text+new_char
        else:
            encrypt_text+=i
    print('Cipher text for '+text+' is '+encrypt_text)

text=input('Enter a Text:')
shift=int(input('Enter any number(1-9):'))
cipher(text,shift)
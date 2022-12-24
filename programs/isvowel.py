#WAP to accept a character from user and check whether it is vowel or consonant.

ch=input('Enter a Character=')
if(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
    if (ch=='A' or ch=='a'or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ch,' is a Vowel')
    else:
        print(ch,'is a Consonant')
else:
    print('Please Enter only Alphbets.')



# WAP to accept a character from user and check whether it is vowel or consonant.

ch=input('Enter a Character=')
if(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
    #if ch in ['a','e','i','o','u','A','E','I','O','U']:
    if ch in 'aeiouAEIOU':
        print(ch,'is a vowel')
    else:
        print(ch,'is a consonant')
else:
    print('Not a letter')


s1=input('Enter a string=')
vowelcnt,consocnt=0,0
capscnt,smallcnt=0,0
numcnt,spcnt,totalcnt=0,0,0
for ch in s1:
    if(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        if ch in 'aeiouAEIOU':
            vowelcnt+=1
        elif(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
            consocnt+=1
        if(ch>='A' and ch<='Z'):
            capscnt+=1
        elif(ch>='a' and ch<='z'):
            smallcnt+=1
    elif(ch>='0' and ch<='9'):
            numcnt+=1
    else:
        spcnt+=1
print('Vowel=',vowelcnt)
print('Consonant=',consocnt)
print('Digits=',numcnt)
print('Special Character=',spcnt)
print('Capital Letters=',capscnt)
print('Small Letters=',smallcnt)
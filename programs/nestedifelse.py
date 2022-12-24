#Condition recruitment company.
# 1.Candidate age must be graeter and 25 years.
# 2.In Final Year Score Must be graeter than 70%.


age=int(input('Enter Your Age='))
if age>=25:
    score=float(input('Enter your Final year Score='))
    if score>=70:
        print('Congratulations! :)\n\tYou are eligible for this Job..!')
    else:
        print('Sorry!You are not eligible for this job..!')
else:
    print('Sorry! You are not eligible for this job')
print('Thank You!')

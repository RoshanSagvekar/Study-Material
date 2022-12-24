"""

"""
# Write a program to accept person's name,pan number,and validate the same using regular expression/regex.

import re
"""
name=input("Enter Name=")
name_pattern="^[a-zA-Z ']*$"
if re.match(name_pattern,name):
    print(name)
else:
    print('Enter a Valid Name.')

email=input("Enter E-mail ID=")
email_pattern="^[a-zA-Z0-9._]*[@][A-Za-z]*[.][A-Za-z]{2,3}$"
if re.match(email_pattern,email):
    print(email)
else:
    print('Enter a Valid Name.')

pan=input('Enter Pan Number=')
pan_pattern="^[A-Z]{5}[0-9]{4}[A-Z]{1}"
if re.match(pan_pattern,pan):
    print(pan)
else:
    print('Enter a Valid Name.')
"""

"""
file=open("email_list.txt","r")
#print(file.read())
#file.seek(0)
emaildata=file.read()
print(emaildata)
file.close()

# The whole string should match the pattern
# print(re.match("^[a-zA-Z0-9._]*[@][A-Za-z]*[.][A-Za-z]{2,3}$",emaildata))

# when you want to identify values in a string as per pattern - findall
# while using findall exclude ^ and $

email_list=re.findall("[a-zA-Z0-9._]*[@][A-Za-z]*[.][A-Za-z]{2,3}",emaildata)
print("List of E-mail")
for email in email_list:
    print(email)
"""


import re

#Return a list containing every occurrence of "ai":


str = "The rain in Spain"

x = re.findall("ai", str)

print(x)


str = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", str)

print(x)


if (x):

  print("Yes, there is at least one match!")

else:

  print("No match")


str = "The rain in Spain"

x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

x = re.split("\s", str,2)

print(x)


x = re.sub("\s", "9", str)

print(x)
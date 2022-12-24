"""
1.	Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T". 
Example: 
            If the file "story.txt" contains the following lines: 
                        A boy is playing there.
                        There is a playground.
                        An aeroplane is in the sky.
                        The sky is pink.
                        Alphabets and numbers are allowed in the password.
The function should display the output as 3.
"""
# my_file=open('story.txt','a')
# my_file.write("A boy is playing there.\nThere is a playground.\nAn aeroplane is in the sky.\nThe sky is pink.\nAlphabets and numbers are allowed in the password.")

def count_line():
    count=0
    my_file=open('story.txt',"r")
    for line in my_file:
        if line[0] not in 'T':
            count+= 1
    my_file.close()
    print("Number of lines without starting with T=",count)

count_line()

# 2. Write a function display_words() in python to read lines from a text file "story.txt",
# and display those words, which are less than 4 characters.
"""

def display_words():
    my_file=open('story.txt','r')
    count=0
    line=my_file.read()
    word=line.split()
    list=[]
    for w in word:
        if len(w)<4:
            list.append(w)
    print(list)
    my_file.close()

display_words()
"""

# 3.Write a function in Python to copy the content of story.txt into story2.txt file. 
"""
def copyf():
    my_file=open('story.txt','r')
    line=my_file.read()
    my_file=open('story2.txt','w')
    my_file.write(line)

copyf()
"""


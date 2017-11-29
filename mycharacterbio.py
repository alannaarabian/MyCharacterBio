#### This is my survey file ####

# These are my questions to be asked in the survey

q1 = 'What is your name? '
q2 = 'Where do you live? '
q3 = 'What is your job? '
q4 = 'What is your biggest fear?'
q5 = 'what is your biggest regret?'
q6 = 'who are the people in your life that you love the most?'
q7 = 'what is a pet peeve of yours?'
q8 = 'what do you do for fun?'
q9= 'what is something you are really good at doing?'
q10 = 'what time of day is it?'
q11 = 'what is the weather like?'





# Gather responses from user in terminal and save

r1 = input(q1)
r2 = input(q2)
r3 = input(q3)
r4 = input(q4)
r5 = input(q5)
r6 = input(q6)
r7 = input(q7)
r8 = input(q8)
r9 = input(q9)
r10 = input(q10)
r11= input(q11)





# open and write to a file (character_bio.txt)

file_name = 'character_bio.text'

f = open(file_name, 'w') # open a file and plan to write on it

# write the questions and resposnes on the file

f.write(q1 + '\n')
f.write(r1 + '\n\n')

f.write(q2 + '\n')
f.write(r2 + '\n\n')

f.write(q3 + '\n')
f.write(r3 + '\n\n')

f.write(q4 + '\n')
f.write(r4 + '\n\n')

f.write(q5 + '\n')
f.write(r5 + '\n\n')

f.write(q6 + '\n')
f.write(r6 + '\n\n')

f.write(q7 + '\n')
f.write(r7 + '\n\n')

f.write(q8 + '\n')
f.write(r8 + '\n\n')

f.write(q9 + '\n')
f.write(r9 + '\n\n')

f.write(q10 + '\n')
f.write(r10 + '\n\n')

f.write(q11 + '\n')
f.write(q11 + '\n\n')
        




        


f.close() # make sure to close the file


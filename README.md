# MyCharacterBio
#### This is my survey file ####

# These are my questions to be asked in the survey

q1 = 'What is your name? '
q2 = 'Where do you live? '
q3 = 'What is your job? '


# Gather responses from user in terminal and save

r1 = input(q1)
r2 = input(q2)
r3 = input(q3)


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


f.close() # make sure to close the file

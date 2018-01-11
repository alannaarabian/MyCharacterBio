#### This is my survey file ####

# These are my questions to be asked in the survey

q1 = 'What is your name? \n' 
q2 = 'Where do you live? \n'
q3 = 'What is your job? \n'
q4 = 'What is your biggest fear? \n'
q5 = 'what is your biggest regret? \n'
q6 = 'who are the people in your life that you love the most? \n'
q7 = 'what is a pet peeve of yours? \n'
q8 = 'what do you do for fun? \n'
q9= 'what is something you are really good at doing? \n'
q10 = 'what time of day is it? \n'
q11 = 'what is the weather like? \n'
q12 = 'what did you study in school or what are you studying in school at the moment? \n'
q13 = 'What is your relationship to the person you are talking to or about? \n'
q14 = 'what is your objective? \n'
q15




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
r12= input(q12)
r13= input(q13)
r14= input(q14)






# open and write to a file (character_bio.txt)

file_name = 'character_bio.html'

f = open(file_name, 'w') # open a file and plan to write on it

# write the questions and resposnes on the file
f.write("<html>")

f.write('<p style = "color: blue">' + q1 + '</p>' )
f.write(r1 + '<br><br>')

f.write(q2 + '<br>')
f.write(r2 + '<br><br>')

f.write(q3 + '<br>')
f.write(r3 + '<br><br>')

f.write(q4 + '<br>')
f.write(r4 + '<br><br>')

f.write(q5 + '<br>')
f.write(r5 + '<br><br>')

f.write(q6 + '<br>')
f.write(r6 + '<br><br>')

f.write(q7 + '<br>')
f.write(r7 + '<br><br>')

f.write(q8 + '<br>')
f.write(r8 + '<br><br>')

f.write(q9 + '<br>')
f.write(r9 + '<br><br>')

f.write(q10 + '<br>')
f.write(r10 + '<br><br>')

f.write(q11 + '<br>')
f.write(r11 + '<br><br>')

f.write(q12 + '<br>')
f.write(r12 + '<br><br>')

f.write(q13 + '<br>')
f.write(q13 + '<br><br>')

f.write(q14 + '<br>')
f.write(r14 + '<br><br>')

f.write("</html>")
        




        


f.close() # make sure to close the file


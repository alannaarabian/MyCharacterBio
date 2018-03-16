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

qlist= [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]

 




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

rlist= [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11]

count=0







# open and write to a file (character_bio.txt)
qstart= '<p style = "color: blue">'
astart= '<p style = "color: red">'


file_name = 'character_bio.html'

f = open(file_name, 'w') # open a file and plan to write on it

# write the questions and resposnes on the file
f.write("<html>")

for i in qlist:
    f.write(qstart + i +'</p>')
    f.write(astart + rlist[count] + '</p>')
    count+=1
    
"""   

f.write(qstart + q1 + '</p>' )
f.write(astart + r1 + '</p>')

f.write(q2 + '</p>')
f.write(r2 + '</p>')

f.write(q3 + '</p>')
f.write(r3 + '</p>')

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
f.write(q11 + '<br><br>')

"""
 
f.write("</html>")
        




        


f.close() # make sure to close the file


#-Assignment-Dictionary
#-ques1:- Create a user defined dictionary and get keys corresponding to the value using for loop. 
a=eval(input('enter dictionary'))
b=(input('enter the value'))
for k,v in a.items():
    if b==v:
        break
print(k)


#-ques2:- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject. 
#Hint: Use nested dictionary to store subjects marks.
a={'arpita':{'maths':100,'physics':90,'chemistry':80},'asmita':{'maths':80,'physics':90,'chemistry':100},'bandita':{'maths':70,'physics':80,'chemistry':90}}
b=input('enter name of student')
for k,v in a.items():
    if b==k:
        print('maths=',a[k]['maths'])
        print('physics=',a[k]['physics'])
        print('chemistry=',a[k]['chemistry'])

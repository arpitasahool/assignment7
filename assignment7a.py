#-Assignment-Dictionary
#-Answer-1 values finding using loops
a=eval(input('enter dictionary'))
b=(input('enter the value'))
for k,v in a.items():
    if b==v:
        break
print(k)


#-Answer-2 User defined nested dictionary
a={'arpita':{'maths':100,'physics':90,'chemistry':80},'asmita':{'maths':80,'physics':90,'chemistry':100},'bandita':{'maths':70,'physics':80,'chemistry':90}}
b=input('enter name of student')
for k,v in a.items():
    if b==k:
        print('maths=',a[k]['maths'])
        print('physics=',a[k]['physics'])
        print('chemistry=',a[k]['chemistry'])

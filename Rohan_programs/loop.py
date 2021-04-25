per_marks=input('Enter percentage Marks:')
per_marks = int(per_marks)
if (per_marks >=60 and per_marks<75):
    grade='Fisrt Class'
elif (per_marks >=75 ):
    grade = 'Distinction'
elif (per_marks >=40 and per_marks < 60):
    grade = 'Second Class'
elif (per_marks < 40):
    grade = 'Fail'
print('Grade is ',grade)

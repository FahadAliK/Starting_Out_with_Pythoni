min_salary = 30000
min_experience = 2
Salary = float(input('Enter your salary'))
Experience = int(input('Enter your experience'))

if Salary >= min_salary:
    if Experience >= min_experience:
        print('You are qualified for the loan')
    else:
        print('You should have minimum experience of',min_experience ,'to qualify')
else:
    print('You must earn minimum of',min_salary,'to be qualified')

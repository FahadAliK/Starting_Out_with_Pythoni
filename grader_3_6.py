grade = float(input('Enter the grade obtained'))

if grade >= 90:
    print('Grade=A')
else:
    if grade >=80:
        print('Grade=B')
    else:
        if grade >= 70:
            print('Grade=C')
        else:
            if grade>= 60:
                print('Grade=D')
            else:
                print('Grade=F')
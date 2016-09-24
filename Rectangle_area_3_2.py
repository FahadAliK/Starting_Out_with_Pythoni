L1 = float(input('Enter length of 1st rectangle'))
B1 = float(input('Enter the breadth of 1st rectangle'))

L2 = float(input('Enter length of 2nd rectangle'))
B2 = float(input('Enter breadth of 2nd rectangle'))

A1 = L1*B1
A2 = L2*B2

if A1 > A2:
    print('First rectangle is bigger')
elif A2 > A1:
    print('Second rectangle is greater')
else:
    print('Both are equal')
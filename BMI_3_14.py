Weight = float(input('Enter your weight\t'))
Height = float(input('Enter your height \t'))

BMI = (Weight/(Height**2))*731
print('%.2f'%BMI)

if BMI >=18.5 and BMI <= 25:
    print('Optimal weight')
elif BMI >25:
    print("Overweight")
elif BMI < 18.5:
    print('Underweight')
else:
    print('Worng input')
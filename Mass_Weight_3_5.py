mass = float(input('Enter the mass \t'))

weight = mass*9.8

if weight > 500:
    print('Overweight')
else:
    if weight < 100:
        print('Underweight')
    else:
        print('OK')
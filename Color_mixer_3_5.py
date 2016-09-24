Color1 = input('Enter the name of the color one \t')
Color2 = input('Enter the name of the second color \t')

if Color1 == 'red' or 'RED' and Color2 == 'blue' or 'BLUE':
    print('purple')
elif Color1 == 'red' or 'RED' and Color2 == 'yellow' or 'YELLOW':
    print('orange')
elif Color1 == 'blue' or 'BLUE' and Color2 == 'yellow' or 'YELLOW':
    print('Green')
else:
    print('Not primary color')
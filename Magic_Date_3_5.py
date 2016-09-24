#Enter all the inputs in numeric form

Day = int(input('Enter the day\t'))
Month = int(input('Enter month\t'))
Year = int(input('Enter year in two digits\t'))

magic = Day*Month

if magic == Year:
    print('Magic date')
else:
    print('No magic date')
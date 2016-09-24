Penny = int(input('Enter no of pennies'))
Nickel = int(input('Enter no of Nickels'))
Dime = int(input('Enter no if Dime'))
Quarter = int(input('Enter no of Quarters'))

Total = Penny+(Nickel*5)+(Dime*10)+(Quarter*25)
print(Total)

if Total == 100:
    print('Congratulation')
elif Total <100:
    print('Amount is less by',100-Total)
else:
    print('Amount was Greater by',Total-100)


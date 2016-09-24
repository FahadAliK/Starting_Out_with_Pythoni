Quantity = int(input('Enter the number of packet purchased'))
price = Quantity*99

if Quantity >= 10 and Quantity<=19:
    Discount = price*0.1
    print(Discount)
    Final_price = price-Discount
    print(Final_price)
elif Quantity >=20 and Quantity <=49:
    Discount = price*0.2
    print(Discount)
    Final_price = price-Discount
    print(Final_price)
elif Quantity >=50 and Quantity <=99:
    Discount = price*0.3
    print(Discount)
    Final_price = price-Discount
    print(Final_price)
elif Quantity >= 100:
    Discount = price * 0.4
    print(Discount)
    Final_price = price - Discount
    print(Final_price)
else:
    print('No discount')
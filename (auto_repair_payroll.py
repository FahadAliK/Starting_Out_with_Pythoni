Working_hours = float(input('Enter the total working hour'))
Pay_rate = float(input('Enter hourly pay rate'))

if Working_hours>40:
    Overtime = Working_hours-40
    Overtime_pay = Overtime*(1.5*Pay_rate)
    Normal_pay = 40*Pay_rate
    print('Pay with overtime = ',Normal_pay+Overtime_pay)
else:
    Usual_pay = Working_hours*Pay_rate
    print('Usual pay rate = ',Usual_pay)
Total_seconds = int(input('Enter no of seconds'))

if Total_seconds >= 60 and Total_seconds < 3600:
    Minute = Total_seconds // 60
    seconds = Total_seconds % 60
    print(Minute)
    print(seconds)
elif Total_seconds >= 3600 and Total_seconds < 86400:
    Hour = Total_seconds // 3600
    Minute = (Total_seconds // 3600) % 60
    seconds = Total_seconds % 60
    print(Hour)
    print(Minute)
    print(seconds)
elif Total_seconds >= 86400:
    Day = Total_seconds // 86400
    Hour = (Total_seconds % 86400) // 3600
    Minute = ((Total_seconds % 86400) % 3600) // 60
    seconds = Total_seconds % 60
    print(Day)
    print(Minute)
    print(Hour)
    print(seconds)

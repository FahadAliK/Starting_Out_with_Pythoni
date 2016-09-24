People = int(input('Enter the no of people attending party \t'))
Hotdogs = int(input('Enter no of hotdogs to be served\t'))

Total_Hotdogs_required = People*Hotdogs

Total_no_hotdogs_packages = (Total_Hotdogs_required//10)+1
print(Total_no_hotdogs_packages)
Total_no_dogbuns_required = (Total_Hotdogs_required//8)+1
print(Total_no_dogbuns_required)

No_of_hotdogs = Total_no_hotdogs_packages*10
No_of_dogbuns = Total_no_dogbuns_required*8

Left_hotdog = No_of_hotdogs-Total_Hotdogs_required
print(Left_hotdog)

Left_dogbuns = No_of_dogbuns-Total_Hotdogs_required
print(Left_dogbuns)
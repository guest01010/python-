#year = int(input("Enter the year : "))
year = 0
for i in range (2026):
    i = year
if year %4 ==0 :
    if  year % 100 == 0 :
        if  year % 400 == 0 :
            print ("Bissextile")
        else :
            print ("nonBissextile")
    else:
        print("Bissextile")
else :
 print ("nonBissextile")
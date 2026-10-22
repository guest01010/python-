year = int(input("enter une annee :"))
est_bissextile = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
print (est_bissextile)

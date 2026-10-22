count = 0
for year in range (2026):

    est_bissextile = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

    if est_bissextile:
        count += 1
print (count)



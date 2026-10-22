import math


a = [int(input("Enter xa : ")), int(input("Enter ya : "))]
b = [int(input("Enter xb : ")), int(input("Enter yb : "))]

print("La distance entre A et B est :", math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2))
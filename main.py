import math

xa = int(input("enter la veleur de xa : "))
ya = int(input("enter la veleur de ya : "))
xb = int(input("enter la veleur de xb : "))
yb = int(input("enter la veleur de yb : "))
dist = math.sqrt((xa-xb)**2 + (ya-yb)**2)
print("la distence entre a et b est : ",dist)
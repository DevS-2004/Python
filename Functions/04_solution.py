import math

def calulate(r):
    return math.pi*r*r, 2*math.pi*r

area, circum = calulate(5)
print(f"Area:{area} \nCircumference:{circum}")
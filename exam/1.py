import math
len = float(input("enter yarn length: "))
diam = float(input("enter yarn diameter: "))
vol = math.pi * math.pow(diam * 2, 2) * len
rad = math.sqrt(3 * vol / (4 * math.pi))
print("coil diameter: ", rad / 2)
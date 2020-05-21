import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
point1 = (x1, y1)
point2 = (x2, y2)
a = point2[0] - point1[0]
b = point2[1] - point1[1]
print(math.sqrt(a*a+b*b))

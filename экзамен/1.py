import math

print('введите длину')
yarn_length = float(input())

print('введите диаметр')
yarn_diam = float(input())

yarnball_vol = math.pi * math.pow(yarn_diam*2, 2) * yarn_length
yarnball_rad = math.sqrt(3*yarnball_vol/(4*math.pi))

print('диаметр клубка')
print(yarnball_rad/2)

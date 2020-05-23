import random
n = []
for i in range(0, 127):
    n.append(random.randint(1, 128))
print(n)
a = [int(x) for x in n if not int(x) % 2]
print(a)

n = int(input("enter a natural number: "))
i = 1
s = 0
while n > i:
    if i % 10 == 3:
        s += i
    i += 1
print("the sum of all numbers ending in 3 and not exceeding", n, ":", s)
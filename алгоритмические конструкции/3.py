num = int(input("enter a natural number: "))
i = 1
sum = 0
while(num > i):
    if (i % 10 == 3):
        sum += i
    i += 1
print ("the sum of all numbers ending in 3 and not exceeding",(num),":",(sum))
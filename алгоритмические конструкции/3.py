num = int(input())
i = 1
sum = 0
while(i < num):
    if (i % 10 == 3):
        sum += i
    i += 1
print(sum)
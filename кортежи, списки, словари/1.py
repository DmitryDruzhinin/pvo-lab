list = [10, 20, 30, 40, 50, 60, 70, 80]
for i, num in enumerate(list):
    if(i == 0):
        continue
    if(i % 2 == 0):
        print(list[i])


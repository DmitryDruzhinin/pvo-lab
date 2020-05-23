a = [10, 20, 30, 40, 50, 60, 70, 80]
for i in range(len(a)):
    if i == 0:
        continue
    elif i % 2 == 0:
        print(a[i])
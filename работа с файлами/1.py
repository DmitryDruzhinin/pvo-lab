file = open("file.txt", "r")
lines_num = 0

for line in file:
    if line.strip():
        lines_num += 1

file.close()
print(lines_num)

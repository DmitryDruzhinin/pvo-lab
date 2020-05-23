f = open("text.txt", "r")
counter = 0
while 1:
    data = f.read(1000)
    if data == "":
        break
    filename = str(counter) + "text.txt"
    out = open(filename, "a")
    out.write(data)
    out.close()
    counter += 1

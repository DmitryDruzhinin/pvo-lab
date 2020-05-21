import random
rand_num = random.randint(1, 100)
file = open("output.txt", "a")
file.write(str(rand_num) + "\n")

file.close()

import random
rndm_num = random.randint(1, 128)
file = open("output.txt", "a")
file.write(str(rndm_num) + "\n")
file.close()

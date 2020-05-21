import random


def clear(list):
    return [num for num in list if num % 2 == 0]


nums = []
for i in range(0, 10):
    nums.append(random.randint(1, 100))
print(nums)

print(clear(nums))

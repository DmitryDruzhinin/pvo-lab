def is_prime(n):
    if(n == 1):
        return False
    else:
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n


num = int(input())
sum = 0
for i in range(1, num):
    if (is_prime(i)):
        sum += i
print(sum)

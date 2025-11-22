import sys, time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def mod_pow(a, b, m):
    r = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            r = (r * a) % m
        a = (a * a) % m
        b //= 2
    return r

def is_carmichael(n):
    if n < 3 or is_prime(n):
        return False
    for a in range(2, n):
        if gcd(a, n) == 1 and mod_pow(a, n - 1, n) != 1:
            return False
    return True

st = time.time()
n = int(input("Enter number: "))
res = is_carmichael(n)
et = time.time()

print("Carmichael:", res)
print("Time for execution:", et - st, "sec")
print("Memory utilised:", sys.getsizeof(n) + sys.getsizeof(res),"bytes")

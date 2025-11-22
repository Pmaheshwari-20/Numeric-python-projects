import time
import sys

def mod_pow(a, e, m):
    r = 1
    a %= m
    while e > 0:
        if e & 1:
            r = (r * a) % m
        a = (a * a) % m
        e >>= 1
    return r

def check(a, d, n, s):
    x = mod_pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    i = 1
    while i < s:
        x = (x * x) % n
        if x == n - 1:
            return True
        i += 1
    return False

def is_prime_mr(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 7, 61):
        if a >= n:
            continue
        if not check(a, d, n, s):
            return False
    return True

t1 = time.time()
n = int(input("Enter n: "))
res = is_prime_mr(n)
t2 = time.time()
mem = sys.getsizeof(n) + sys.getsizeof(res) + sys.getsizeof(t1) + sys.getsizeof(t2)
print("Prime?:", res)
print("Time:", t2 - t1)
print("Memory (bytes):", mem)


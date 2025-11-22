import time
import sys

def mod_mul(a, b, m):
    return (a * b) % m

def mod_pow(x, n, m):
    r = 1
    x %= m
    while n > 0:
        if n & 1:
            r = (r * x) % m
        x = (x * x) % m
        n >>= 1
    return r

def is_prime(n):
    if n < 2:
        return False
    small_primes = (2,3,5,7,11,13,17,19,23,29)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for a in (2,7,61):
        if a % n == 0:
            continue
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        skip = False
        for _ in range(s - 1):
            x = mod_mul(x, x, n)
            if x == n - 1:
                skip = True
                break
        if skip:
            continue
        return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n
    x = 2
    y = 2
    c = 1
    d = 1
    while d == 1:
        x = (mod_mul(x, x, n) + c) % n
        y = (mod_mul(y, y, n) + c) % n
        y = (mod_mul(y, y, n) + c) % n
        d = gcd(x - y if x > y else y - x, n)
    if d == n:
        return pollard_rho(n + 1)
    return d

def factor(n):
    if n == 1:
        return
    if is_prime(n):
        print(n)
        return
    f = pollard_rho(n)
    factor(f)
    factor(n // f)

start = time.time()
n = int(input("Enter n to factor: "))
print("Prime factors:")
factor(n)
end = time.time()

mem = sys.getsizeof(n) + sys.getsizeof(start) + sys.getsizeof(end)
print("Execution time:", end - start)
print("Approx memory used (bytes):", mem)


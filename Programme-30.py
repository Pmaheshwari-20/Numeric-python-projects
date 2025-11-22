#Programme-5
from math import isqrt
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def is_fibonacci_prime(n):
    def is_perfect_square(x):
        s = isqrt(x)
        return s * s == x
    if n < 2:
        return False
    fib_check = is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
    prime_check = True
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            prime_check = False
            break
    return fib_check and prime_check
x=is_fibonacci_prime(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(is_fibonacci_prime(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

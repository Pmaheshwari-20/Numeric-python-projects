# Write a function is_pronic(n) that checks if a number is the product of two consecutive integers.

import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def is_pronic(n):
    if n < 0:
        return False
    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i += 1
    return False
x=is_pronic(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(is_pronic(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

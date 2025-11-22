#Programme-2
import math
import time,sys
x=int(input("Enter the remainder:"))
y=int(input("Enter the modulus:"))
st=time.perf_counter()
def crt(x, y):
    if len(x) != len(y):
        raise ValueError("Remainders and moduli lists must have the same length.")
    M = 1
    for m in y:
        M *= m
    total = 0
    for r, m in zip(x, y):
        Mi = M // m 
        inv = pow(Mi, -1, m)
        total += r * Mi * inv
    return total % M
t=crt(x, y)
print(t)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(x)+sys.getsizeof(y)
mem_count = sys.getsizeof(crt(x, y))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

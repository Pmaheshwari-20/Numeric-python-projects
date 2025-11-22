#Programme-4
from math import gcd
import time,sys
a=int(input("Enter the first value:"))
n=int(input("Enter the second value:"))
st=time.perf_counter()
def order_mod(a, n):
    if gcd(a, n) != 1:
        raise ValueError("a and n must be coprime for multiplicative order to exist.")
    k = 1
    value = a % n
    while value != 1:
        value = (value * a) % n
        k += 1
        if k > n:  
            return None
    return k
x=order_mod(a,n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(a)+sys.getsizeof(n)
mem_count = sys.getsizeof(order_mod(a,n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

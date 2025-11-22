#Programme-1
import time,sys
a=int(input("Enter the first value:"))
m=int(input("Enter the second value:"))
st=time.perf_counter()
def mod_inverse(a, m):
    if m <= 0:
        raise ValueError("Modulus m must be a positive integer.")
    a = a % m
    r0, r1 = m, a
    s0, s1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    gcd = r0
    if gcd != 1:
        return None 
    inv = s0 % m
    return inv
x=mod_inverse(a,m)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(a)+sys.getsizeof(m)
mem_count = sys.getsizeof(mod_inverse(a,m))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

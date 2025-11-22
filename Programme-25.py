#Programme-5
import time,sys
n1=int(input("Enter the base:"))
n2=int(input("Enter the exponent:"))
n3=int(input("Enter the modulus:"))
st=time.perf_counter()
def mod_exp(n1,n2,n3):
    r = 1
    n1 = n1 % n3  # Reduce base initially
    while n2 > 0:
        if n2 % 2 == 1:  # If exponent is odd
            r = (r * n1) % n3
        n2 = n2 // 2
        n1=(n1 * n1) % n3
    return r
x=mod_exp(n1,n2,n3)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n1)+sys.getsizeof(n2)+sys.getsizeof(n3)
mem_count = sys.getsizeof(mod_exp(n1,n2,n3))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

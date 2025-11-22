#Programme-3
import time,sys
a=int(input("Enter the first value:"))
p=int(input("Enter the second value:"))
st=time.perf_counter()
def is_quadratic_residue(a, p):
    if p <= 2:
        raise ValueError("p must be an odd prime.")
    a = a % p  
    if a == 0:
        return True  
    result = pow(a, (p - 1) // 2, p)
    if result == 1:
        return True
    elif result == p - 1:
        return False
    else:
        return False
x=is_quadratic_residue(a,p)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(a)+sys.getsizeof(p)
mem_count = sys.getsizeof(is_quadratic_residue(a,p))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

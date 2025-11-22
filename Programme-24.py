#Programme-4
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def is_highly_composite(n):
    max_divisors = 0
    for i in range(1, n):
        divisors_i = sum(1 for j in range(1, i + 1) if i % j == 0)
        if divisors_i > max_divisors:
            max_divisors = divisors_i
    
    divisors_n = sum(1 for j in range(1, n + 1) if n % j == 0)
    return divisors_n > max_divisors
x=is_highly_composite(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(is_highly_composite(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

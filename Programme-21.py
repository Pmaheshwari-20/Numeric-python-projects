#Programme-1
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def aliquot_sum(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=i
    return c
x=aliquot_sum(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(aliquot_sum(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

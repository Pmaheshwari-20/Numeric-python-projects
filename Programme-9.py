#Programme-4
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
l1=list()
r=1
def digital_root(n):
    if n==0:
        return 0
    return 1+(n-1)%9
x=digital_root(n)
print("The digital root of the number is:",x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(digital_root(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

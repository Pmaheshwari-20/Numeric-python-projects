#Programme-5
import time,sys
n=int(input("Enter a number:"))
st=time.perf_counter()
def is_abundant(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=i
    if c>n:
        return "True"
    else:
        return "False"
x=is_abundant(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(is_abundant(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

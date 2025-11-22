#Programme-3
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def multiplicative_persistence(n):
    c=0
    while n >= 10:  
        p=1
        for digit in str(n):
            p*= int(digit)
        n = p
        c+=1
    return c
x=multiplicative_persistence(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(multiplicative_persistence(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

#Programme-3
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def mean_of_digits(n):
    c=0
    for i in str(n):
        c+=int(i)
    return c/len(str(n))
x=mean_of_digits(n)
print("The aveage mean of the digits of the number is:",x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(mean_of_digits(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

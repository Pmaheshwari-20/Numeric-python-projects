#Write a function is_automorphic(n) that checks if a number's square ends with the number itself.
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def is_automorphic(n):
    x=n**2
    if n<0:
        return "Not Automorphic!"
    if str(x).endswith(str(n)):
        return "Automorphic!"
    else:
        return "Not Automorphic!"
x=is_automorphic(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(is_automorphic(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

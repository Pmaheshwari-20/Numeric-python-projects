#Write a function for harshad number is_harshad(n) that checks if a number is divisible by the sum of its digits.
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def is_harshad(n):
    c=0
    if n<0:
        return "Not Harshad!"
    for i in str(n):
        c+=int(i)
    if n%c==0:
        return "Harshad!"
    else:
        return "Not Harshad!"
x=is_harshad(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(is_harshad(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

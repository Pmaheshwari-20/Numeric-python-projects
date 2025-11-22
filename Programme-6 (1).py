#Programme-1
import time,sys
n=int(input("Enter the number whose factorial you want to calculate:"))
st=time.perf_counter()
def factorial(n):
    if n<0:
        print("Negative integer, factorial calculation not possible!")
    else:
        fact=1
        while n!=0:
            fact*=n
            n-=1
    return fact
x=factorial(n)
print("The factorial of the number is;",x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(factorial(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

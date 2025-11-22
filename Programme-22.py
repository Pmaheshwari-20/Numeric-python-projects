#Programme-2
import time,sys
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
st=time.perf_counter()
def are_amicable(a, b):
    sum_a = sum(i for i in range(1, a) if a % i == 0)
    sum_b = sum(i for i in range(1, b) if b % i == 0)
    return sum_a==b and sum_b==a
x=are_amicable(a,b)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(a)+sys.getsizeof(b)
mem_count = sys.getsizeof(are_amicable(a,b))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

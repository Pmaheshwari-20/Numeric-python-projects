#Programme number-3
import sys
import time
n=int(input("Enter the number whose factor sum you want to calculate:"))
st=time.perf_counter()
def divisor_sum(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=i
    return c
a=divisor_sum(n)
et=time.perf_counter()
ent=et-st
print("The sum of the factors of the number is:",a)
print(f"Program execution time:{ent:4f}seconds")
print("Memory utilized",sys.getsizeof(divisor_sum(n),"Bytes"))

## Write a function is_deficient(n) that returns True if the sum of proper divisors of n is less than n.
import time,sys
n=(int(input("Enter a number :  ")))
st=time.perf_counter()

def is_deficient(n):
    sum=0
    for i in range(1,n):
        if n%i ==0:
            sum= sum+i
            if (sum<n):
             return True
            else:
             return False

x=is_deficient(n)
print(x)
et=time.perf_counter()
ttime=et-st
print(f"Program execution time:{ttime:4f}seconds")
mem_n=sys.getsizeof(n)
mem_count=sys.getsizeof(is_deficient(n))
mem_total=mem_n+mem_count
print("memory utilised:",mem_total,"bytes")

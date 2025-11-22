# Write a function prime_factors(n) that returns the list of prime factors of a number..

import time,sys
n=int(input("Enter the number :"))
st=time.perf_counter()
def prime_factors(n):
    prime = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        prime.append(n)
    return prime
x=prime_factors(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n= sys.getsizeof(n)
mem_count= sys.getsizeof(prime_factors(n))
mem_total= mem_n + mem_count
print("memory used:",mem_total,"bytes")

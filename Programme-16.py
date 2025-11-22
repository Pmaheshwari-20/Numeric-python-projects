#Write a function count_distinct_prime_factors(n) that returns how many unique prime factors a number has.

import time, sys

start = time.perf_counter()
def count_distinct_prime_factors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1
    return count
    
while True:
    x = input("Enter a number (or 'end' to stop): ")
    if x.lower() == "end":
        break
    if not x.isdigit() or int(x) <= 0:
        print("Invalid input. Try again.")
        continue
    n = int(x)
    
    result = count_distinct_prime_factors(n)
    end = time.perf_counter()
    ttime= end - start
    print("Distinct prime factors:", result)
    print(f"Program execution time:{ttime:4f}seconds")
    print("Memory used:", sys.getsizeof(result), "bytes")
   

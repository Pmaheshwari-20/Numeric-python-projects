# Write a function is_prime_power(n) that checks if a number can be expressed as pk where p is prime and k ≥ 1.

import time, sys
start = time.perf_counter()
def is_prime_power(n):
    if n < 2:
        return False
    for p in range(2, n + 1):
        k = 1
        power = p ** k
        while power <= n:
            if power == n:
                return True
            k += 1
            power = p ** k
    return False

while True:
    x = input("Enter a number (or 'end' to stop): ")
    if x.lower() == "end":
        break
    if not x.isdigit() or int(x) <= 0:
        print("Invalid input. Try again.")
        continue
    n = int(x)
   
    result = is_prime_power(n)
    end = time.perf_counter()
    ttime= end - start
    print("Prime Power:", result)
    print(f"execution time:{ttime:4f} seconds ")
    print("Memory used:", sys.getsizeof(result), "bytes")

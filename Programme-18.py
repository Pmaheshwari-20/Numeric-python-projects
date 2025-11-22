# Write a function is_mersenne_prime(p) that checks if 	2p – 1 is a prime number (given that p is prime).

import time, sys
start = time.perf_counter()

def is_mersenne_prime(p):
    if p < 2:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    n = 2 ** p - 1
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True

while True:
    x = input("Enter a prime number p (or 'end' to stop): ")
    if x.lower() == "end":
        break
    if not x.isdigit() or int(x) <= 0:
        print("Invalid input. Try again.")
        continue
    p = int(x)
    result = is_mersenne_prime(p)
    end = time.perf_counter()
    ttime= end - start
    print("Mersenne prime check:", result)
    print(f"Program execution time: {ttime:4f} seconds")
    print("Memory used:", sys.getsizeof(result), "bytes")

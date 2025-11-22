# Write a function twin_primes(limit) that generates all twin prime pairs up to a given limit.

import time, sys
start = time.perf_counter()

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def twin_primes(limit):
    pairs = []
    for i in range(2, limit - 1):
        if is_prime(i) and is_prime(i + 2):
            pairs.append((i, i + 2))
    return pairs

while True:
    x = input("Enter limit (or 'end' to stop): ")
    if x.lower() == "end":
        break
    if not x.isdigit() or int(x) <= 2:
        print("Invalid input. Try again.")
        continue
    limit = int(x)
    result = twin_primes(limit)
    end = time.perf_counter()
    ttime= end - start
    print("Twin primes up to", limit, ":", result)
    print(f"Program execution time: {ttime:4f} seconds")
    print("Memory used:", sys.getsizeof(result), "bytes")

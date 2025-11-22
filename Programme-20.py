#Write a function Number of Divisors (d(n)) count_divisors(n) that returns how many positive divisors a number has.

import time, sys
start = time.perf_counter()

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
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
    result = count_divisors(n)
    end = time.perf_counter()
    ttime= end - start
    print("Number of divisors:", result)
    print(f'Program execution time: {ttime:4f} seconds')
    print("Memory used:", sys.getsizeof(result), "bytes")


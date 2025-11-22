import sys, time
def collatz_length(n):
    c = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        c += 1
    return c

st = time.time()
n = int(input("Enter number: "))
steps = collatz_length(n)
et = time.time()

print("Collatz Length:", steps)
print("Time for execution:", et - st, "sec")
print("Memory utilised:", sys.getsizeof(n) + sys.getsizeof(steps),"bytes")

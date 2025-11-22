import sys, time
def is_perfect_power(n):
    for a in range(2, n):
        p = a * a
        while p <= n:
            if p == n:
                return True
            p *= a
    return False

st = time.time()
n = int(input("Enter number: "))
res = is_perfect_power(n)
et = time.time()

print("Perfect Power:", res)
print("Time for execution:", et - st, "sec")
print("Memory utilised:", sys.getsizeof(n) + sys.getsizeof(res),"bytes")

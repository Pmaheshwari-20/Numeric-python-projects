import time, sys

def partition_function(nv):
    if nv < 0:
        return 0
    arr = [0] * (nv + 1)
    arr[0] = 1
    i = 1
    while i <= nv:
        s = 0
        k = 1
        while True:
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2
            if g1 > i and g2 > i:
                break
            sg = 1 if (k % 2 == 1) else -1
            if g1 <= i:
                s += sg * arr[i - g1]
            if g2 <= i:
                s += sg * arr[i - g2]
            k += 1
        arr[i] = s
        i += 1
    return arr[nv]

t0 = time.time()
num = int(input("Enter n: "))
out = partition_function(num)
t1 = time.time()

print("p(n):", out)
print("Execution time:", t1 - t0)

mem = (
    sys.getsizeof(num) +
    sys.getsizeof(out) +
    sys.getsizeof(t0) +
    sys.getsizeof(t1) +
    sys.getsizeof([0])
)
print("Approx memory used (bytes):", mem)

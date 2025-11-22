import sys, time
def polygonal_number(s, n):
    return ((s - 2) * n * n - (s - 4) * n) // 2

st = time.time()
s = int(input("Enter s (sides): "))
n = int(input("Enter n (term): "))
p = polygonal_number(s, n)
et = time.time()

print("Polygonal Number:", p)
print("Time for execution:", et - st, "sec")
print("Memory utilised:", sys.getsizeof(s) + sys.getsizeof(n) + sys.getsizeof(p),"bytes")

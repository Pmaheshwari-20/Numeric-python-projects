import sys, time
def lucas_sequence(n):
    a, b = 2, 1
    print("The Lucas sequence is:", end=" ")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

st = time.time()
n = int(input("Enter n: "))
lucas_sequence(n)
et = time.time()

print("\nTime for execution:", et - st, "sec")
print("Memory utilised:", sys.getsizeof(n) + sys.getsizeof(st) + sys.getsizeof(et),"bytes")

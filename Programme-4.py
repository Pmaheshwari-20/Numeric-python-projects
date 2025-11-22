#Programme number-4
import time,sys
print("Prime Counting Program (π(n))")
n=int(input("Enter n: "))
def prime_pi(n):
    start=time.time()
    count=1
    for i in range(2,n+1):
        fact=True
        for j in range(2,n+1):
            if i%j==0:
                fact=False
                break
            if fact:
                count+=1
                break
    end = time.time()
    mem = sys.getsizeof(n) + sys.getsizeof(count)
    print("π(n):", count)
    print("Execution time:", round(end-start, 5), "seconds")
    print("Memory used:", mem, "bytes\\n")
prime_pi(n)

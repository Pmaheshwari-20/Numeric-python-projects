#Programme-5
import time,sys
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def modular_pow(a, b, m):
    result=1
    base=a%m
    exp=b
    while exp>0:
        if exp%2==1:
            result=(result*base)%m
        
        exp=exp//2
    return result

def legendre_symbol(a, p):
    start_time=time.time()
    power=(p-1)//2
    value=modular_pow(a,power,p)
    if value==p-1:
        symbol=-1
    elif value==1:
        symbol=1
    else:
        symbol=0
    end_time=time.time()
    memory_used=sys.getsizeof(a)+sys.getsizeof(p)+sys.getsizeof(power)+sys.getsizeof(value)+sys.getsizeof(symbol)
    print("\\n--- Results ---")
    print("Legendre Symbol (a/p):", symbol)
    print("Execution Time (seconds):", end_time - start_time)
    print("Total Memory Used (bytes):", memory_used)
    print("-------------------------\\n")

while True:
    print("Enter 0 as 'a' to exit the program.\\n")
    n=int(input("Enter value of n: "))
    if n==0:
        print("Exiting program.")
        break
    p=int(input("Enter an odd prime p: "))
    if p%2==0 or not is_prime(p):
        print("Error: p must be an odd prime number. Please try again.\\n")
        continue
    is_prime(n)
    modular_pow(n,b,m)
    legendre_symbol(n,p)

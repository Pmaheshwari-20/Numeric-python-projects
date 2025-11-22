#Programme-2
import time,sys
n=int(input("Enter the number:"))
st=time.perf_counter()
def is_palindrome(n):
    st1=''
    for i in range(len(str(n))-1,-1,-1):
        st1+=str(n)[i]
    if st1==str(n):
        return "Yes, the number is a palindrome!"
    else:
        return "No, the number is not a palindrome!"        
x=is_palindrome(n)
print(x)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
mem_n = sys.getsizeof(n)
mem_count = sys.getsizeof(is_palindrome(n))
mem_total = mem_n + mem_count
print("Approximate memory used (bytes):", mem_total)

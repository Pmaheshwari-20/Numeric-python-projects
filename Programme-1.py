#Programme number-1
import sys
import time
n=int(input("Enter the number whose Euler's Totient you want to calculate:"))
l1=list()
l2=list()
l3=list()
st=time.perf_counter()
def euler_phi(n):
    for i in range(1,n):
        l1.append(i)
    for j in l1:
        x=j
        y=n
        val=x%y
        while val!=0:
            val=x%y
            x,y=y,val
            l2.append(val)
        if l2[len(l2)-2]==1:
            l3.append(j)
    return len(l3)
a=euler_phi(n)
print("The Euler's totient of the number is:",a)
et=time.perf_counter()
ent=et-st
print(f"Program execution time:{ent:4f}seconds")
print("Memory utilized",sys.getsizeof(euler_phi(n)),"Bytes")

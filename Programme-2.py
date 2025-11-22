#Programme number-2
import sys
import time
n=int(input("Enter the number whose mobius function you want to calculate:"))
l1=list()
l2=list()
c1=0
c2=0
st=time.perf_counter()
def mobius(n):
    x=2
    y=3
    while n%x==0:
        l1.append(x)
        n//=x
    while y*y<=n:
        while n%y==0:
            l1.append(y)
            n//=y
        y+=2
    if n>2:
        l1.append(n)
    for i in l1:
        if i not in l2:
            l2.append(i)
    if len(l2)!=len(l1):
        a=0
        return a
    else:
        if len(l2)%2==0:
            b=1
            return b
        else:
            b1=-1
            return b1
x=mobius(n)
et=time.perf_counter()
ent=et-st
print("The mobius value of the function is:",x)
print(f"Program execu21on time:{ent:4f}seconds")
print("Memory utilized",sys.getsizeof(mobius(n)),"Bytes")

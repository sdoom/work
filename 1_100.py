import math
def isPrime(m):
    n=math.sqrt(m)
    n=int(n)
    while n>1:
        if m%n==0:
            break
        n-=1
    else:
        print(m)
L = list(range(100))
for x in L[2:99]:
    isPrime(x)

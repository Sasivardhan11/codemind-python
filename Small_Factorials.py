import math
t=int(input())
fact=1
for i in range(t):
    n=int(input())
    for j in range(1,n+1):
        fact=math.factorial(j)
    print(fact)
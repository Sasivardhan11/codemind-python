n=int(input())
f=0
if n>1:
    for i in range(2,int(n/2)):
        if n%i==0:
            f=0
            break
        else:
            f=1
if f==1:
    print("prime")
else:
    print("not a prime")
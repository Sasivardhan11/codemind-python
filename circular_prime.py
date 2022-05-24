n=int(input())
s=0
f=0
a=0
if n>1:
    for i in range(2,int(n/2)):
        if n%i==0:
            f=0
            break
        else:
            f=1
while n>0:
    s=s*10+n%10
    n=n//10
if s>1:
    for i in range(2,int(s/2)):
        if s%i==0:
            a=0
            break
        else:
            a=1
if (f==1 and a==1):
    print("circular prime")
elif (f==1 or a==1):
    print("prime but not a circular prime")
else:
    print("not prime")
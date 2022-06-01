n=int(input())
temp=n
s=0
p=1
while n>0:
    r=n%10
    s=s+r
    n=n//10
while temp>0:
    r1=temp%10
    p=p*r1
    temp=temp//10
a=p-s
print(a)
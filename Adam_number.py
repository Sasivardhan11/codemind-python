n=int(input())
s,su=0,0
a=n*n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
rev=s*s
while rev>0:
    b=rev%10
    su=su*10+b
    rev=rev//10
if a==su:
    print("True")
else:
    print("False")
m=int(input())
s1=0
s2=0
s3=0
while m>0:
    r1=m%10
    s1=s1+r1
    m=m//10
while s1>0:
    r2=s1%10
    s2=s2+r2
    s1=s1//10
while s2>0:
    r3=s2%10
    s3=s3+r3
    s2=s2//10
print(int(s3))
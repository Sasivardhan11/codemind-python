t=int(input())
for i in range(t):
    n=int(input())
    temp=n
    a=int(n**(1/2))
    p=a*a
    if p==temp:
        print("True")
    else:
        print("False")
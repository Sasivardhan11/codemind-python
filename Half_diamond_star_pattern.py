n=int(input())
if (3<=n<=100):
    for i in range(n-1):
        for j in range(i+1):
            print("*",end='')
        print()
    for i in range(n):
        for j in range(i,n):
            print("*",end='')
        print()
else:
    print("The pattern is not possible")
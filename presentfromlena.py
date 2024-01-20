def line(n):
    if n==0:
        print(0,end='')
    else:
        for i in range(2*n+1):
            if i<=n:
                print(i,end=' ')
            else:
                if i==2*n:
                    print(2*n-i,end="")
                else:
                    print(2*n-i,end=" ")
    print()
m=int(input())
for j in range(2*m+1):
    if j<=m:
        print("  "*(m-j),end="")
        line(j)
    else:
        print("  "*(j-m),end="")
        line(2*m-j)

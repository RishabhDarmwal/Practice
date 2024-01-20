#A. Ambitious Kid
n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    if lst[i]<0:
        lst[i]=abs(lst[i])
print(min(lst))
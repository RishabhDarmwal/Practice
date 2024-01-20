n = int(input())
lst=list(map(int, input().split()))
c=0
m=lst.index(min(lst))
M=max(lst)
for i in range(n):
    if lst[i]==min(lst):
        m=i
if m!=n-1:
    c+=n-1-m
    mn=lst.pop(m)
    lst.append(mn)
if lst.index(M)!=0:
    c+=lst.index(M)
print(c)
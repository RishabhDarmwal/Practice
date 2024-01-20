
n=int(input())
s=input()
a=b=0
for i in s:
    if i==b:
        a+=1
    b=i
print(a)
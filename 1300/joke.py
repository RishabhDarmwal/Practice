a=input();b=input();c=list(input())
d=list(a+b)
o=0
if len(d)==len(c):
    for i in d:
        if i in c and d.count(i)==c.count(i):
            o=1
        else:
            o=0
            break
if o==0:
    print("NO")
elif o==1:
    print("YES")

        
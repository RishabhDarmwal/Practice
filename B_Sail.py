t,sx,sy,ex,ey=map(int,input().split())
s=input()
dx=ex-sx
dy=ey-sy

if dx!=0:
    dirx=dx/abs(dx)
    if dirx==1:
        x='E'
    else:
        x='W'
elif dx==0:
    x=''
if dy!=0:
    diry=dy/abs(dy)
    if diry==1:
        y='N'
    else:
        y='S'
elif dy==0:
    y=''
if s.count(x)<abs(dx) or s.count(y)<abs(dy):
    print(-1)
else:
    lst=[]
    total=0;tx=0;ty=0;c=0
    i=0
    while total<abs(dx)+abs(dy) and i<t:
        char=s[i]
        i+=1
        if tx<abs(dx):
            if char==x:
                total+=1
                tx+=1
        if ty<abs(dy):
            if char==y:
                total+=1
                ty+=1  
    print(i)
        

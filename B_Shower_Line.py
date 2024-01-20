from itertools import permutations
m=[[*map(int,input().split())] for _ in ' '*5]
sum=lambda x,y: m[x][y]+m[y][x]
print(max(sum(a,b)+sum(b,c)+2*(sum(c,d)+sum(d,e)) for a,b,c,d,e in permutations(range(5))))

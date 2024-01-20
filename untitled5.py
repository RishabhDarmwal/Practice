# cook your dish here

from itertools import permutations 
         
def printAll( st):
     
    # Number of subsequences is (2**n -1)
    n = len(st)
    opsize = pow(2, n)
    p=[]
    # Generate all subsequences of a given string.
    #  using counter 000..1 to 111..1
    for counter in range(1, opsize):
     
        subs = ""
        for j in range(n):
         
            # Check if jth bit in the counter is set
            #   If set then print jth element from arr[] 
            if (counter & (1<<j)):
                subs += (st[j])
  
        # Print all permutations of current subsequence 
        perm = permutations(subs)
        for i in perm:
            word=''.join(i)
            p.append(word) 
    return p
def islex(st):
    l=list(st)
    a=l.copy()
    l.sort()
    if a==l:
        return True
    else:
        return False

for i in range(int(input())):
    N=int(input())
    s=input()
    al=set(printAll(s))
    c=0
    for j in al:
        z=list(j)
        for k in z:
            if j.count(k)>s.count(k):
                c1=0
                break
        else:
            c1=1
        
        if c1==1 and islex(j):
            c+=1
        
    print(c)
        

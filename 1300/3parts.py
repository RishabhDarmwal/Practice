# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:05:38 2023

@author: risha
"""

def print_three_parts(N):
    # Traversing to choose first part
    if N<7:
        return None
    if N%3==1:
        part1=(N-1)//3
        part2=(N-1)//3
        part3=(N-1)//3
    if N%3==1:
        part1=(N-1)//3
        part2=(N-1)//3
        part3=(N-1)//3+1
    if N%3==2:
        part1=(N-1)//3
        part2=(N-1)//3
        part3=(N-1)//3+2
    while part1==part2 or part2==part3 or part2%3==0 or part1%3==0:
        part1-=1
        part2+=1
    while part3==part2 or part1==part3 or part3%3==0 or part1%3==0:
        part1-=1
        part3+=1
    while part1==part2 or part1==part3 or part1%3==0 or part2%3==0:
        part2-=1
        part1+=1
    return (f'YES\n{part1} {part2} {part3}')
                    
 
# Driver Code
if __name__ == "__main__":
    for i in range(int(input())):
        N = int(input())
        if print_three_parts(N)==None:
            print("NO")
        
        else:
            print(print_three_parts(N))


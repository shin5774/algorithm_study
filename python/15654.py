import sys
from itertools import permutations

sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=sorted(list(map(int,sys_input().rstrip().split())))
ans=list(permutations(arr,M))

for p in ans:
    for x in p:
        print(x,end=" ")
    print()

import sys
from itertools import permutations

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

arr=sorted(list(map(int,sys_input().rstrip().split())))

ans=sorted(list(set(permutations(arr,m))))

for a in ans:
    for x in a:
        print(x,end=" ")
    print()

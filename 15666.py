import sys
from collections import deque
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=sorted(list(set(map(int,sys_input().rstrip().split()))))

ans=deque()

def problem(idx,level):
    if level==M:
        for x in ans:
            print(x,end=" ")
        print()

    else:
        for i in range(idx,len(arr)):
            ans.append(arr[i])
            problem(i,level+1)
            ans.pop()

problem(0,0)

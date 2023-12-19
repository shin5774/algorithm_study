import sys
from itertools import combinations
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())


# 1번 풀이:itertools 사용
for ans in combinations(range(1,n+1),m):
    for x in ans:
        print(x,end=" ")

    print()


# 2번 풀이: backtracking 사용
arr=[i for i in range(1,n+1)]
ans=[]

def back_tracking(prev):
    if len(ans)==m:
        for x in ans:
            print(x,end=" ")
        print()
        return

    if m-len(ans)>n-1-prev:
        return

    for i in range(prev+1,n):
        ans.append(arr[i])
        back_tracking(i)
        ans.pop()

back_tracking(-1)

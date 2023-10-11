import sys
from itertools import permutations

sys_input=sys.stdin.readline

n=int(sys_input())
k=int(sys_input())
arr=[sys_input().rstrip() for _ in range(n)]

ans=set()
for x in permutations(arr,k): #경우의수를 다 찾음
    ans.add(''.join(x)) #집합에 넣음으로서 중복을 무시

print(len(ans))

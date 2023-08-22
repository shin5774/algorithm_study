import sys
from collections import deque
sys_input=sys.stdin.readline

n=int(sys_input())
arr=deque(map(int,sys_input().rstrip().split()))
stack=deque()
idx=1
success=True

while idx<=n:
    p_idx=idx
    if len(stack)!=0 and stack[-1]==idx:
        stack.pop()
        idx+=1
    else:
        while len(arr)!=0:
            if arr[0]==idx:
                arr.popleft()
                idx+=1
                break
            else:
                stack.append(arr[0])
                arr.popleft()

    if p_idx==idx:
        success=False
        break

if success:
    print("Nice")
else:
    print("Sad")

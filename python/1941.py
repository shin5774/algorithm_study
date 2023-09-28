import sys
from itertools import combinations
from collections import deque

sys_input=sys.stdin.readline
all_seats=[(i,j) for i in range(5) for j in range(5)]
arr=[sys_input().rstrip() for _ in range(5)]
ans=0

def connected(seats):
    s=set(seats)
    visited=set()

    q=deque()
    q.append(seats[0])

    while q:
        x,y=q.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if nx<0 or nx>=5 or ny<0 or ny>=5:
                continue

            if (nx,ny) not in visited and (nx,ny) in s:
                q.append((nx,ny))

    if len(visited)!=7:
        return False

    return True



for cur in combinations(all_seats,7):
    if not connected(cur):
        continue

    cnt=0
    for x,y in cur:
        if arr[x][y]=='S':
            cnt+=1

    if cnt>=4:
        ans+=1

print(ans)

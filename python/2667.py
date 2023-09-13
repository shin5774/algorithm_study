import sys
from collections import deque

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())

mv=[[1,0],[-1,0],[0,1],[0,-1]]

arr=[[]*n for _ in range(n)]
total=0
ans=[]

def bfs(x,y):
    arr[x][y]='0'
    q=deque()
    q.append([x,y])
    cnt=0
    while (len(q)!=0):
        cx,cy=q.pop()
        cnt+=1

        for sx,sy in mv:
            tx=cx+sx
            ty=cy+sy

            if tx<0 or ty<0 or tx>=n or ty>=n:
                continue
            if arr[tx][ty]=='1':
                q.append([tx,ty])
                arr[tx][ty]='0'

    return cnt

for i in range(n):
    for x in sys_input().rstrip():
        arr[i].append(x)

for i in range(n):
    for j in range(n):
        if arr[i][j]=='1':
            total+=1
            ans.append(bfs(i,j))

print(total)
ans.sort()

for a in ans:
    print(a)

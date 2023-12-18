import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
arr=[[0]*101 for _ in range(101)]

for _ in range(n):
    x1,y1,x2,y2=map(int,sys_input().rstrip().split())

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            arr[x][y]+=1


ans=0

for x in range(101):
    for y in range(101):
        if(arr[x][y]>m):
            ans+=1

print(ans)

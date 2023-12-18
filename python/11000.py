import sys
from heapq import heappush,heappop
sys_input=sys.stdin.readline
classes=[]
rooms=[]

n=int(sys_input())

for _ in range(n):
    s,e=map(int,sys_input().rstrip().split())
    heappush(classes,(s,e))

while classes:
    s,e=heappop(classes)

    if rooms and s>=rooms[0]:
        heappop(rooms)

    heappush(rooms,e)

print(len(rooms))

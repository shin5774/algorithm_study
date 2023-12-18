import sys
from collections import deque
sys_input=sys.stdin.readline

n,w,l=map(int,sys_input().rstrip().split())
cars=deque(map(int,sys_input().rstrip().split()))
bridge=deque()
bridge_cur=0
t=0

for _ in range(w-1):
    bridge.append(0)

while cars:
    car=cars.popleft()

    if len(bridge)==w:
        bridge_cur-=bridge.popleft()

    if bridge_cur+car<=l:
        bridge.append(car)
        bridge_cur+=car
    else:
        cars.appendleft(car)
        bridge.append(0)

    t+=1


while bridge_cur!=0:
    bridge_cur-=bridge.popleft()
    t+=1

print(t)

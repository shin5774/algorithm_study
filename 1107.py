import sys
sys_input=sys.stdin.readline

N=int(sys_input())
M=int(sys_input())
if M==0:
    broken=set()
else:
    broken=set(map(int,sys_input().rstrip().split()))

ans=abs(int(N)-100)

#upscale
for i in range(N,1000000):
    si=str(i)
    trigger=False
    for x in range(len(si)):
        if int(si[x]) in broken:
            trigger=True
            break

    if not trigger and len(si)+abs(int(si)-N)<ans:
        ans=len(si)+abs(int(si)-N)
        break

#downscale

for i in range(N,-1,-1):
    si=str(i)
    trigger=False
    for x in range(len(si)):
        if int(si[x]) in broken:
            trigger=True
            break

    if not trigger and len(si)+abs(int(si)-N)<ans:
        ans=len(si)+abs(int(si)-N)
        break

print(ans)

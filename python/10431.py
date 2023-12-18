import sys
sys_input=sys.stdin.readline

def problem():
    input=list(map(int,sys_input().rstrip().split()))
    tc=input[0]
    arr=input[1:]
    ans=0
    cur=[]

    for x in arr:
        if not cur or cur[-1]<x :
            cur.append(x)
            continue

        for idx in range(len(cur)):
            if cur[idx]>x:
                ans+=len(cur)-idx
                cur[idx+1:]=cur[idx:]
                cur[idx]=x
                break

    print(tc,ans)


for _ in range(int(sys_input())):
    problem()

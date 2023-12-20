import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

ans=[]

def back_tracking(prev):
    if len(ans)==m:
        for x in ans:
            print(x,end=" ")
        print()
        return

    for i in range(prev,n+1):
        ans.append(i)
        back_tracking(i)
        ans.pop()

back_tracking(1)

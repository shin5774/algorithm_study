import sys
sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    func=sys_input().rstrip()
    n=int(sys_input())
    pos,rpos,cnt=0,n,0
    reverse=False

    arr=list(sys_input().rstrip()[1:-1].split(","))
    ans=""

    for f in func:
        if f=='D':
            cnt=cnt+1

            if cnt>n:
                print("error")
                return

            if reverse:
                rpos=rpos-1
            else:
                pos=pos+1

        else:
            reverse=not reverse


    ans=ans+"["

    if reverse:
        for i in range(rpos-1,pos-1,-1):
            ans=ans+arr[i]+","

    else:
        for i in range(pos,rpos):
            ans=ans+arr[i]+","

    if n-cnt>0:
        ans=ans[:-1]
    ans=ans+"]"

    print(ans)

for _ in range(T):
    problem()

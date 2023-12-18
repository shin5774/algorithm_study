import sys
sys_input=sys.stdin.readline

while True:
    try:
        n,b,m=map(float,sys_input().rstrip().split())
        ans=0

        while n<=m:
            n*=(1+b*0.01)
            ans+=1

        print(ans)
    except:
        break

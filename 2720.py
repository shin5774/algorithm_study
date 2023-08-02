import sys
sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    C=int(sys_input())
    ans=[0,0,0,0]
    val=[25,10,5,1]

    for i in range(4):
        ans[i]+=C//val[i]
        C-=val[i]*ans[i]

    for x in ans:
        print(x,end=" ")

    print()



for _ in range(T):
    problem()

import sys
sys_input=sys.stdin.readline

problem=dict()
s_num=0
ans=0

while True:
    input=list(sys_input().rstrip().split())

    if input[0]=='-1':
        break

    t,p,res=int(input[0]),input[1],input[2]

    if res=='right':
        s_num+=1
        if p in problem:
            ans+=t+problem[p]*20
        else:
            ans+=t
    else:
        if p not in problem:
            problem[p]=0

        problem[p]+=1

print(s_num,ans)

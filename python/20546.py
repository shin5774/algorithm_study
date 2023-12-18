import sys
sys_input=sys.stdin.readline

cash=int(sys_input())
days=list(map(int,sys_input().rstrip().split()))

def find_bnp():
    cur=cash
    cnt=0

    for day in days:
        if day<=cur:
            cnt+=cur//day
            cur%=day

    return cur+cnt*days[-1]

def find_timing():
    cur=cash
    cnt=0

    down_cnt=0
    up_cnt=0

    for idx in range(1,len(days)):
        if days[idx]>days[idx-1]:
            up_cnt+=1
            down_cnt=0
        elif days[idx]<days[idx-1]:
            up_cnt=0
            down_cnt+=1
        else:
            up_cnt=0
            down_cnt=0

        if up_cnt>=3:
            cur+=days[idx]*cnt
            cnt=0

        if down_cnt>=3:
            cnt+=cur//days[idx]
            cur%=days[idx]

    return cur+cnt*days[-1]

bnp,timing=find_bnp(),find_timing()

if bnp>timing:
    print("BNP")
elif bnp<timing:
    print("TIMING")
else:
    print("SAMESAME")

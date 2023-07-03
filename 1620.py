import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
pton={} #포켓몬 -> 번호
ntop={} #번호 -> 포켓몬

for i in range(1,n+1):
    name=sys_input().rstrip()
    pton[name]=i
    ntop[i]=name

for _ in range(m):
    q=sys_input().rstrip()
    if q[0]<'0' or q[0]>'9': #숫자인지 확인하는 과정
        print(pton[q])
    else:
        print(ntop[int(q)])

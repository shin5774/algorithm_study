import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
pton={} #���ϸ� -> ��ȣ
ntop={} #��ȣ -> ���ϸ�

for i in range(1,n+1):
    name=sys_input().rstrip()
    pton[name]=i
    ntop[i]=name

for _ in range(m):
    q=sys_input().rstrip()
    if q[0]<'0' or q[0]>'9': #�������� Ȯ���ϴ� ����
        print(pton[q])
    else:
        print(ntop[int(q)])

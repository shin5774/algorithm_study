import sys
from queue import PriorityQueue

sys_input=sys.stdin.readline

n=int(sys_input().rstrip())
arr=list(map(int,sys_input().rstrip().split()))
ans=[0]*n
Q=PriorityQueue() #�������� ������ ���� �켱����ť ����

for i in range(n):
    Q.put((arr[i],i))

cur_num=0
p_num=0
is_first=True

while Q.qsize()!=0: #���� �Է� ����
    x,idx=Q.get()
    if is_first:
        ans[idx]=cur_num
        p_num=x
        is_first=False
        continue
    if x!=p_num:
        cur_num=cur_num+1
        p_num=x
    ans[idx]=cur_num

for x in ans:
    print(x,end=" ")

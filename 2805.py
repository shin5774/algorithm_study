import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())
trees=sorted(list(map(int,sys_input().rstrip().split()))) #���ı��� ��Ŵ

end=trees[-1] #���� ū���� ������ ���� or ���� �Ƚ�ų�Ÿ� max(trees)�ص���
start=1

while start<=end:
    mid=(start+end)//2
    cur=0
    for t in trees:
        if t>mid:
            cur+=t-mid

    if cur>m:
        start=mid+1
    elif cur<m:
        end=mid-1
    else:
        start=start+1

print(end) #start�� while�� Ż���ϱ⿡ end�� ���̵�

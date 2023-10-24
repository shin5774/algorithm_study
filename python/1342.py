import sys
sys_input=sys.stdin.readline

s=sys_input().rstrip()
d=dict() #알파벳 개수
ans=0

for x in s:
    if x not in d:
        d[x]=0
    d[x]+=1


def find(level,before):
    if level==len(s):
        global ans
        ans+=1
        return

    for x in d.keys():
        if d[x]==0:
            continue
        if x==before: #이전과 같은지 확인
            continue

        d[x]-=1
        find(level+1,x)
        d[x]+=1

find(0,"")

print(ans)

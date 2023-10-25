import sys
sys_input=sys.stdin.readline

n=int(sys_input())
d=dict()
cur=[] #스택
ans=0

for i in range(n):
    d[sys_input().rstrip()]=i #들어온 순서 넣어주기


for _ in range(n):
    output_num=d[sys_input().rstrip()]

    #추월했다면 역순으로 되어있다 ex)4132 -> 4와 3이 추월함. 따라서 나온 순서를 스택에 넣고 오름차순이 아니라면 앞 차량은 추월을 한것이다.
    while cur and cur[-1]>output_num:
        ans+=1
        cur.pop()

    cur.append(output_num)

print(ans)

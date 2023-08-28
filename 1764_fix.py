import sys

sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

#각 입력값을 집합에 넣어줌
a=set([sys_input().rstrip() for _ in range(n)])
b=set([sys_input().rstrip() for _ in range(m)])

ans=list(a&b) #두 집합의 교집합을 list에 넣음
ans.sort() #해당 list를 정렬함

print(len(ans))

for name in ans:
    print(name)

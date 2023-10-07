import sys
from collections import deque

sys_input=sys.stdin.readline

n=int(sys_input())
t=0 #현재 시간

for _ in range(n):
    a,b=map(int,sys_input().rstrip().split()) #a/b

    if t<b: #현재시간이 최초 봇이 나타난 시간 이전인 경우
        t=b+1
        continue

    cur=(t-b)%(a+b) #(a+b)=> 반복되는 초수,(t-b)=>최초 봇이 돌아가고 남은 시간

    if cur<a: #대기시간인 경우
        t+=1
    else: #봇 탐지 시간인 경우
        t+=(a+b)-cur+1 #(a+b)-cur=> 현재 시간부터 봇이 사라지기까지 걸리는 시간

print(t)

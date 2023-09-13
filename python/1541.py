import sys
sys_input=sys.stdin.readline

input=sys_input().rstrip().split("-") #뺄셈 기호 기준으로 1차 분리
a_input=[]

for i in input:
    a_input.append(sum(map(int,(i.split("+"))))) #좌항부터 순서대로 계산

answer=a_input[0]

for i in range(1,len(a_input)): #계산한값들을 순서대로 빼줌
    answer-=a_input[i]

print(answer)

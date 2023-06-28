import sys
sys_input=sys.stdin.readline

input=sys_input().rstrip().split("-")
a_input=[]

for i in input:
    a_input.append(sum(map(int,(i.split("+")))))

answer=a_input[0]

for i in range(1,len(a_input)):
    answer-=a_input[i]

print(answer)

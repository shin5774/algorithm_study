import sys
from collections import deque

sys_input=sys.stdin.readline

input=sys_input().rstrip()
c_input=deque()
n=deque()
oper=deque()
brank=deque()
ans=deque()

i=0
while i<len(input):
    if (input[i]=='*' or input[i]=='/') and input[i+1]!='(':

        a=c_input.pop()
        c_input.append('(')
        c_input.append(a)
        c_input.append(input[i])
        c_input.append(input[i+1])
        c_input.append(')')
        i+=2

    else:
        c_input.append(input[i])
        i+=1


for i in range(len(c_input)):
    if c_input[i]=='(':
        brank.append(c_input[i])
    elif c_input[i]==')':
        brank.pop()
        for _ in range(2):
            ans.appendleft(n.pop())
        ans.append(oper.pop())

    elif c_input[i]=='+' or c_input[i]=='-' or c_input[i]=='*' or c_input[i]=='/':
        oper.append(c_input[i])
    else:
        n.append(c_input[i])

if len(n)>len(oper):
    for _ in range(2):
        ans.append(n.popleft())
    ans.append(oper.pop())
else:
    while len(n)!=0:
        ans.appendleft(n.popleft())
        ans.append(oper.popleft())

for x in ans:
    print(x,end="")

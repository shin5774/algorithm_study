import sys
from collections import deque
sys_input=sys.stdin.readline

arr=sys_input().rstrip()

n=deque()
op=deque()

for i in range(len(arr)):
    if arr[i]=='(':
        op.append(arr[i])

    elif arr[i]=='*' or arr[i]=='/':
        if len(op)!=0 and (op[-1]=='*' or op[-1]=='/'):
            cop=op.pop()
            y=n.pop()
            x=n.pop()
            result=''.join(x)
            result+=y
            result+=cop
            n.append(result)


        op.append(arr[i])

    elif arr[i]=='+' or arr[i]=='-':
        while len(op)!=0 and op[-1]!='(':
            cop=op.pop()
            y=n.pop()
            x=n.pop()
            result=''.join(x)
            result+=y
            result+=cop
            n.append(result)

        op.append(arr[i])

    elif arr[i]==')':
        #괄호까지 계산
        while True:
            cop=op.pop()
            if cop=='(':
                break

            y=n.pop()
            x=n.pop()

            result=''.join(x)
            result+=y
            result+=cop
            n.append(result)
    else:
        n.append(arr[i])


while len(op)!=0:
    cop=op.pop()

    y=n.pop()
    x=n.pop()
    result=''.join(x)
    result+=y
    result+=cop
    n.append(result)


print(n[0])

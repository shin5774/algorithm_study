import sys
from collections import deque
sys_input=sys.stdin.readline

def find(a,b):
    if a=='A':
        if b=='A':
            return 'A'
        elif b=='G':
            return 'C'
        elif b=='C':
            return 'A'
        else:
            return 'G'
    elif a=='G':
        if b=='A':
            return 'C'
        elif b=='G':
            return 'G'
        elif b=='C':
            return 'T'
        else:
            return 'A'
    elif a=='G':
        if b=='A':
            return 'A'
        elif b=='G':
            return 'T'
        elif b=='C':
            return 'C'
        else:
            return 'G'
    else:
        if b=='A':
            return 'G'
        elif b=='G':
            return 'A'
        elif b=='C':
            return 'G'
        else:
            return 'T'

n=int(sys_input())
ans=deque()
for x in sys_input().rstrip():
    ans.append(x)

while len(ans)!=1:
    a=ans.pop()
    b=ans.pop()
    ans.append(find(a,b))
    print(ans)

print(ans[0])

import sys
sys_input=sys.stdin.readline

d,p=0,0

for _ in range(int(sys_input())):
    w=sys_input().rstrip()

    if abs(d-p)==2:
        continue

    if w=='D':
        d+=1
    else:
        p+=1


print(d,end=":")
print(p)

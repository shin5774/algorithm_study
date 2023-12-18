import sys
sys_input=sys.stdin.readline

def end(a,b,c,d):
    return not (a==b and b==c and c==d)

def problem(a,b,c,d):
    cur=0

    while end(a,b,c,d):
        a,b,c,d=abs(a-b),abs(b-c),abs(c-d),abs(d-a)
        cur+=1

    return cur

while True:
    a,b,c,d=map(int,sys_input().rstrip().split())

    if a==0 and b==0 and c==0 and d==0:
        break

    print(problem(a,b,c,d))

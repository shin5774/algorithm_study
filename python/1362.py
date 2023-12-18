import sys
sys_input=sys.stdin.readline
case=1

def problem(o,w):
    while True:
        op,n=sys_input().rstrip().split()

        if op=='#' and n=='0':
            break

        if w>0:
            if op=='E':
                w-=int(n)
            else:
                w+=int(n)

    if w<=0:
        return "RIP"

    if w>o*0.5 and w<o*2:
        return ":-)"

    return ":-("

while True:
    o,w=map(int,sys_input().rstrip().split())

    if o==0 and w==0:
        break

    print(case,problem(o,w))
    case+=1

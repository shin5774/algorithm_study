import sys
sys_input=sys.stdin.readline

N=int(sys_input())
s=set()
fs=set([str(i) for i in range(1,21)])

for _ in range(N):
    line=sys_input().rstrip().split()

    if line[0]=="add":
        s.add(line[1])
    elif line[0]=="remove":
        if line[1] in s:
            s.remove(line[1])
    elif line[0]=="check":
        if line[1] in s:
            print(1)
        else:
            print(0)
    elif line[0]=="toggle":
        if line[1] in s:
            s.remove(line[1])
        else:
            s.add(line[1])
    elif line[0]=="all":
        s=set(fs)
    else:
        s=set()

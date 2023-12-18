import sys
sys_input=sys.stdin.readline

s=set()
move=list()
ans=True

def calc(cur,before):
    if abs(ord(cur[0])-ord(before[0]))==1:
        if abs(ord(cur[1])-ord(before[1]))!=2:
            return False
    elif abs(ord(cur[0])-ord(before[0]))==2:
        if abs(ord(cur[1])-ord(before[1]))!=1:
            return False
    else:
        return False

    return True

for _ in range(36):
    input=sys_input().rstrip()

    if move:
        before=move[-1]

        if ans:
            ans=calc(input,before)

    move.append(input)
    s.add(input)


if ans:
    ans=calc(move[0],move[-1])


if (len(s)==36) and ans:
    print("Valid")
else:
    print("Invalid")

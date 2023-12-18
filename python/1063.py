import sys
sys_input=sys.stdin.readline

n=int(sys_input())
one=int(sys_input())
other=[int(sys_input()) for _ in range(n-1)]
ans=0

if n==1:
    print(0)
    exit()

while True:
    max_num=max(other)

    if one>max_num:
        break

    elif one==max_num:
        ans+=1
        break

    max_idx=other.index(max_num)

    one+=1
    other[max_idx]-=1
    ans+=1


print(ans)

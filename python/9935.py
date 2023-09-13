import sys

sys_input=sys.stdin.readline

arr=sys_input().rstrip()
e_arr=sys_input().rstrip()

ans=[]

for i in range(len(arr)):
    ans.append(arr[i])
    if ''.join(ans[-len(e_arr):])==e_arr:
        for _ in range(len(e_arr)):
            ans.pop()

if len(ans)==0:
    print("FRULA")
else:
    for x in ans:
        print(x,end="")

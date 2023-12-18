import sys
sys_input=sys.stdin.readline

arr=[int(sys_input()) for _ in range(5)]
ans=0

if arr[0]<0:
    ans+=abs(arr[0])*arr[2]
    ans+=arr[3]
    ans+=arr[1]*arr[4]

else:
    ans+=(arr[1]-arr[0])*arr[4]

print(ans)

import sys
sys_input=sys.stdin.readline

N=int(sys_input())
arr=[]
inter=[]

def bcd(a,b):
    if b==0:
        return a
    return bcd(b,a%b)

for _ in range(N):
    arr.append(int(sys_input()))

for i in range(0,len(arr)-1):
    inter.append(arr[i+1]-arr[i])

mbcd=bcd(inter[1],inter[0])

for i in range(1,len(inter)-1):
    cur=bcd(inter[i+1],inter[i])

    if mbcd>cur:
        mbcd=bcd(mbcd,cur)
    else:
        mbcd=bcd(cur,mbcd)


ans=0
for x in inter:
    ans+=x//mbcd-1

print(ans)

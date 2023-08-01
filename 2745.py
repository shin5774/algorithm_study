import sys
sys_input=sys.stdin.readline

N,B=sys_input().rstrip().split()

B=int(B)
ans=0
p=0
for i in range(len(N)-1,-1,-1):
    cur=ord(N[i])
    if cur>=ord('0') and cur<=ord('9'):
        ans+=(cur-ord('0'))*int(pow(B,p))
    else:
        ans+=(cur-ord('A')+10)*int(pow(B,p))
    
    p+=1

print(ans)
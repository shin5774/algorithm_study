import sys
sys_input=sys.stdin.readline

n,m=map(int,sys_input().rstrip().split())

game=[1001]
ans=dict()

for _ in range(n):
    game.append(int(sys_input()))

for _ in range(m):
    lim=int(sys_input())

    for i in range(1,len(game)):
        if game[i]<=lim:
            if i not in ans:
                ans[i]=0
            ans[i]+=1
            break

print(max(ans,key=ans.get))

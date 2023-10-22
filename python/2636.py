import sys
sys_input=sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m=map(int,sys_input().rstrip().split())

arr=[]
cheeze=set() #치즈의 위치
turn=[] #i번째 턴의 남은 치즈의 수

#initialize and input
for i in range(n):
    l=list(map(int,sys_input().rstrip().split()))

    for j in range(m):
        if l[j]==1:
            cheeze.add((i,j))

    arr.append(l)

turn.append(len(cheeze))

def is_air(x,y): #공기와 만남,즉 배열의 맨 끝에 도달했는가를 알려줌
    if x==0 or x==n-1 or y==0 or y==m-1:
        return True

    return False

def is_remove(x,y,visited):
    visited[x][y]=True

    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if visited[nx][ny] or arr[nx][ny]==1:
            continue

        if is_air(nx,ny):
            return True

        if (is_remove(nx,ny,visited)): #상,하,좌,우중 하나라도 공기에 닿으면 해당 치즈는 제거 대상
            return True

    return False

def play_turn():
    remove=[] #이번 턴에 제거되는 치즈의 좌표

    for ch in cheeze:
        visited=[[False]*m for _ in range(n)] #dfs를 위한 방문 체크

        if(is_remove(ch[0],ch[1],visited)):
            remove.append(ch)

    turn.append(turn[-1]-len(remove)) #이전턴의 치즈수에서 현재 제거해야할 치즈수

    for ch in remove:
        arr[ch[0]][ch[1]]=0 #0으로 만들어줌
        cheeze.remove(ch) #치즈 제거


#치즈가 사라지기 전까지 반복
while turn[-1]!=0:
    play_turn()

print(len(turn)-1)
print(turn[-2])

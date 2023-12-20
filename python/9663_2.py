import sys
sys_input=sys.stdin.readline

n=int(sys_input())
cur=[]
ans=0

def success(row,col):
    for x,y in cur:
        if col==y or row+col==x+y or row-col==x-y:
            return False

    return True

def back_tracking(level):
    if len(cur)==n:
        global ans
        ans+=1

        return

    for i in range(1,n+1):
        if success(level,i):
            cur.append((level,i))
            back_tracking(level+1)
            cur.pop()

back_tracking(1)
print(ans)

import sys
sys_input=sys.stdin.readline

T=int(sys_input())

def len_check(a,b):
    cur=0
    for i in range(4):
        if a[i]!=b[i]:
            cur+=1
    return cur

def problem():
    n=int(sys_input())
    mbti=sys_input().rstrip().split()
    mset=set(mbti)
    dlist=[]
    mdict=dict()

    for i in mbti:
        if i not in mdict:
            mdict[i]=0
        mdict[i]+=1

        if mdict[i]==3:
            return 0

    if len(mset)==1:
        return 0

    #2
    ans=1e9
    if n!=len(mset):
        for i in mset:
            if mdict[i]!=2:
                continue
            for j in mset:
                if i==j:
                    continue

                cnt=0
                for k in range(4):
                    if i[k]!=j[k]:
                        cnt+=1
                cnt*=2
                if cnt<ans:
                    ans=cnt

    #1
    for i in mset:
        for j in mset:
            if i==j:
                continue
            for k in mset:
                if i==k or j==k:
                    continue
                cur=len_check(i,j)+len_check(j,k)+len_check(i,k)

                ans=min(ans,cur)


    return ans


for _ in range(T):
    print(problem())

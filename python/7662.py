import sys,heapq

sys_input=sys.stdin.readline

T=int(sys_input())

def problem():
    max_h=[]
    min_h=[]
    minside_del=dict()
    maxside_del=dict()
    k=int(sys_input())
    cnt=0

    for _ in range(k):
        op,n=sys_input().rstrip().split()

        if op=="I":
            heapq.heappush(min_h,int(n))
            heapq.heappush(max_h,(-int(n),int(n)))
            cnt=cnt+1
        else:
            if cnt==0:
                continue

            if n=="1":
                while True:
                    if max_h[0][1] not in minside_del:
                        if max_h[0][1] not in maxside_del:
                            maxside_del[max_h[0][1]]=0
                        maxside_del[max_h[0][1]]=maxside_del[max_h[0][1]]+1

                        heapq.heappop(max_h)
                        break
                    else:
                        if minside_del[max_h[0][1]]==1:
                            del(minside_del[max_h[0][1]])
                        else:
                            minside_del[max_h[0][1]]=minside_del[max_h[0][1]]-1
                        heapq.heappop(max_h)
            else:
                while True:
                    if min_h[0] not in maxside_del:
                        if min_h[0] not in minside_del:
                            minside_del[min_h[0]]=0
                        minside_del[min_h[0]]=minside_del[min_h[0]]+1
                        heapq.heappop(min_h)
                        break
                    else:
                        if maxside_del[min_h[0]]==1:
                            del(maxside_del[min_h[0]])
                        else:
                           maxside_del[min_h[0]]=maxside_del[min_h[0]]-1
                        heapq.heappop(min_h)
            cnt=cnt-1

    if cnt==0:
        print("EMPTY")
    else:
        min_ans=heapq.heappop(min_h)

        while min_ans in maxside_del:
            maxside_del[min_ans]=maxside_del[min_ans]-1
            if maxside_del[min_ans]==0:
                del(maxside_del[min_ans])
            min_ans=heapq.heappop(min_h)

        max_ans=heapq.heappop(max_h)[1]

        while max_ans in minside_del:
            minside_del[max_ans]=minside_del[max_ans]-1
            if minside_del[max_ans]==0:
                del(minside_del[max_ans])
            max_ans=heapq.heappop(max_h)[1]

        print(max_ans,min_ans)

for _ in range(T):
    problem()

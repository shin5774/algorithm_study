import sys,math

sys_input=sys.stdin.readline

n=int(sys_input())

input=list(map(int,sys_input().rstrip().split()))
visited=[False]*(n+1) #남은 숫자 확인용

#소문제 1
if input[0]==1:
    k=input[1]
    ans=[]
    cur=n-1
    while k>1:
        #개수 확인
        cur_fact=math.factorial(cur)
        cnt=1 #개수

        while k>cur_fact*cnt:
            cnt+=1
        cnt-=1

        #개수만큼 빼기
        k-=cur_fact*cnt

        #사용하지 않은 수중 개수에 맞는수를 정답에 넣음
        for i in range(1,n+1):
            if visited[i]:
                continue

            if cnt==0:
                ans.append(i)
                visited[i]=True
                break

            cnt-=1

        cur-=1

    #남은거 넣기
    for i in range(1,n+1):
        if visited[i]:
            continue
        ans.append(i)

    for x in ans:
        print(x,end=" ")

#소문제 2
else:
    find=input[1:]
    ans=0
    for idx in range(len(find)-1):
        x=find[idx]
        cnt=0
        for i in range(1,n+1):
            if visited[i]:
                continue

            if i==x:
                visited[i]=True
                ans+=math.factorial(n-idx-1)*cnt #개수 더하기
                break

            cnt+=1

    print(ans+1)

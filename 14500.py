import sys
sys_input=sys.stdin.readline

N,M=map(int,sys_input().rstrip().split())
arr=[list(map(int,sys_input().rstrip().split())) for _ in range(N)]
blocks=[
    [ #line
      [(0,1),(0,2),(0,3),(0,3)],
      [(1,0),(2,0),(3,0),(3,0)]
    ],
    [ #block
      [(0,1),(1,0),(1,1),(1,1)]
    ],
    [ #L
      [(-1,0),(-2,0),(0,1),(-2,1)],
      [(0,1),(0,2),(1,0),(1,2)],
      [(0,-1),(1,0),(2,0),(2,-1)],
      [(-1,0),(0,-1),(0,-2),(-1,-2)],
      [(-1,0),(-2,0),(0,-1),(-2,-1)],
      [(-1,0),(0,1),(0,2),(-1,2)],
      [(0,1),(1,0),(2,0),(2,1)],
      [(1,0),(0,-1),(0,-2),(1,-2)]
    ],
    [ #z
      [(1,0),(1,1),(2,1),(2,1)],
      [(0,1),(1,1),(1,2),(1,2)],
      [(1,0),(1,-1),(2,-1),(2,-1)],
      [(0,-1),(1,-1),(1,-2),(1,-2)]

    ],
    [ #else
      [(0,1),(0,2),(1,1),(1,2)],
      [(-1,0),(-2,0),(-1,1),(-2,1)],
      [(0,-1),(0,-2),(-1,-1),(-1,-2)],
      [(1,0),(2,0),(1,-1),(2,-1)]
    ],

]
ans=0

def out_range(i,j):
    global N,M
    if i<0 or j<0 or i>=N or j>=M:
        return True
    return False

def find(i,j):
    global blocks,arr,ans

    for block in blocks:
        for rot_block in block:
            li,lj=rot_block[-1]
            if out_range(i+li,j+lj):
                continue
            sum=arr[i][j]
            for ni,nj in rot_block[:3]:
                sum=sum+arr[i+ni][j+nj]

            if sum>ans:
                ans=sum

    return

for i in range(N):
    for j in range(M):
        find(i,j)

print(ans)

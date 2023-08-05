import sys
sys_input=sys.stdin.readline
x=set()
y=set()
input=[]

for _ in range(3):
    a,b=map(int,sys_input().rstrip().split())
    x.add(a)
    y.add(b)
    input.append((a,b))

def find():
    for i in x:
        for j in y:
            if (i,j) in input:
                continue
            print(i,j)
            return


find()

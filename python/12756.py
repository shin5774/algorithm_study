import sys
sys_input=sys.stdin.readline

aa,ah=map(int,sys_input().rstrip().split())
ba,bh=map(int,sys_input().rstrip().split())

while ah>0 and bh>0:
    ah-=ba
    bh-=aa

if ah<=0 and bh<=0:
    print("DRAW")
elif ah<=0:
    print("PLAYER B")
else:
    print("PLAYER A")

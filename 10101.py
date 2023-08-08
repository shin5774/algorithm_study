import sys
sys_input=sys.stdin.readline

s=set()
sum=0
for _ in range(3):
    n=int(sys_input())
    s.add(n)
    sum+=n

if sum!=180:
    print("Error")
elif len(s)==1:
    print("Equilateral")
elif len(s)==2:
    print("Isosceles")
else:
    print("Scalene")

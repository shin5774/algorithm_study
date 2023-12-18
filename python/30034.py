import sys
sys_input=sys.stdin.readline

delim=set()

for _ in range(2):
    n=int(sys_input())
    for x in sys_input().rstrip().split():
        delim.add(x)

n=int(sys_input())
for x in sys_input().rstrip().split():
    if x in delim:
        delim.remove(x)

n=int(sys_input())
input=sys_input().rstrip()

for x in delim:
    input=input.replace(x,' ')

for x in input.split():
    print(x)

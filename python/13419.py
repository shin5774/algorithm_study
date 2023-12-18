import sys
from collections import deque
sys_input=sys.stdin.readline


for _ in range(int(sys_input())):
    input=sys_input().rstrip()

    if len(input)==1:
        for _ in range(2):
            print(input)

        continue

    even=input[0::2]
    odd=input[1::2]

    if len(input)%2==0:
        print(even)
        print(odd)

    else:
        print(even+odd)
        print(odd+even)

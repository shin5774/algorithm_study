import sys
sys_input=sys.stdin.readline

input=sys_input().rstrip()
arr=[1,0,0,2]

for x in input:
    if x=='A':
        arr[0],arr[1]=arr[1],arr[0]
    elif x=='B':
        arr[0],arr[2]=arr[2],arr[0]
    elif x=='C':
        arr[0],arr[3]=arr[3],arr[0]
    elif x=='D':
        arr[1],arr[2]=arr[2],arr[1]
    elif x=='E':
        arr[1],arr[3]=arr[3],arr[1]
    else:
        arr[2],arr[3]=arr[3],arr[2]

print(arr.index(1)+1)
print(arr.index(2)+1)

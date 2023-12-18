import sys
sys_input=sys.stdin.readline

p=set()
k=set()
h=set()
t=set()

input=sys_input().rstrip()

for i in range(0,len(input)-2,3):
    op=input[i]
    num=int(input[i+1:i+3])

    if op=="P":
        if num in p:
            print("GRESKA")
            exit()

        p.add(num)

    elif op=="K":
        if num in k:
            print("GRESKA")
            exit()

        k.add(num)

    elif op=="H":
        if num in h:
            print("GRESKA")
            exit()

        h.add(num)

    else:
        if num in t:
            print("GRESKA")
            exit()

        t.add(num)

print(13-len(p),13-len(k),13-len(h),13-len(t))

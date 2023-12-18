import sys
sys_input=sys.stdin.readline

start,end,finish=sys_input().rstrip().split()
start=start.split(":")
end=end.split(":")
finish=finish.split(":")

print(start,end,finish)

before=set()
after=set()

def compare(a_h,a_m,b_h,b_m):
    if a_h<b_h:
        return False

    if a_h>b_h:
        return True

    if a_m<=b_m:
        return False
    else:
        return True

while True:
    try:
        time,name=sys_input().rstrip().split()
        hour,min=time.split(":")

        if not compare(hour,min,start[0],start[1]):
            before.add(name)
        elif (hour==end[0] and min==end[1]) or (compare(hour,min,end[0],end[1]) and not compare(hour,min,finish[0],finish[1])):
            after.add(name)

    except:
        break

print(len(before&after))

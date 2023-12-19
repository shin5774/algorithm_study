import sys
sys_input=sys.stdin.readline

y=2014
m=4
d=1

n=int(sys_input())

def is_leap_year():
    return (y%4==0 and y%100!=0) or y%400==0

def find_day_limit():
    if (m<8 and m%2==1) or (m>=8 and m%2==0):
        return 31
    elif m==2:
        if is_leap_year():
            return 29
        return 28
    else:
        return 30

def convert(n):
    if n<10:
        return "0"+str(n)
    else:
        return str(n)

while n>0:
    day_lim=find_day_limit()

    if d+n>day_lim:
        n-=day_lim-d
        d=0
        m+=1

        if m==13:
            m=1
            y+=1

    else:
        d+=n
        break

print(str(y)+"-"+convert(m)+"-"+convert(d))

import sys
sys_input=sys.stdin.readline

l,c=map(int,sys_input().rstrip().split())
arr=sorted(list(map(str,sys_input().rstrip().split())))
const_n,vow_n=0,0 #자음,모음수
b_set=set(['a','e','i','o','u'])
cur=[]

def is_vowel(x):
    return x in b_set

def next_add_find(idx):
    cur.append(arr[idx])
    find(idx+1)
    cur.pop()

def find(idx):
    global const_n,vow_n,c

    if len(cur)==l:
        if const_n>=2 and vow_n>=1:
            print(''.join(cur))
        return

    if idx==c:
        return

    is_v=is_vowel(arr[idx])

    if is_v:
        vow_n+=1
        next_add_find(idx)
        vow_n-=1
    else:
        const_n+=1
        next_add_find(idx)
        const_n-=1

    find(idx+1)

find(0)

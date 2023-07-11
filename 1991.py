import sys
sys_input=sys.stdin.readline

N=int(sys_input())
tree=[[] for _ in range(N)]

for _ in range(N):
    p,l,r=sys_input().rstrip().split()

    tree[ord(p)-ord("A")].append(p)
    tree[ord(p)-ord("A")].append(l)
    tree[ord(p)-ord("A")].append(r)
#pre
def pre(idx):
    print(tree[idx][0],end="")

    if tree[idx][1]!=".":
        pre(ord(tree[idx][1])-ord("A"))

    if tree[idx][2]!=".":
        pre(ord(tree[idx][2])-ord("A"))
#in
def inorder(idx):
    if tree[idx][1]!=".":
        inorder(ord(tree[idx][1])-ord("A"))

    print(tree[idx][0],end="")

    if tree[idx][2]!=".":
       inorder(ord(tree[idx][2])-ord("A"))
#post
def post(idx):
    if tree[idx][1]!=".":
        post(ord(tree[idx][1])-ord("A"))

    if tree[idx][2]!=".":
        post(ord(tree[idx][2])-ord("A"))

    print(tree[idx][0],end="")

pre(0)
print()
inorder(0)
print()
post(0)

import sys
sys_input=sys.stdin.readline

tree=dict()
cnt=0

while True:
    input=sys_input().rstrip()
    if not input: #sys_input()인 경우 입력 탈출을 위함.
        break

    if input not in tree: #딕셔너리에 없으면 추가
        tree[input]=0
    tree[input]+=1
    cnt+=1

#key들을 정렬후 f-string을 이용해 반올림(round는 0.5의 경우 오류가 발생하므로 사용 x))
for x in sorted(tree.keys()):
   print(f'{x} {tree[x]/cnt*100:.4f}')

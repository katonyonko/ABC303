import io
import sys

_INPUT = """\
6
4 2 3 1
RUDL
-1 -1
1 0
5 2 1 5
LDRLD
0 0
-1 -1
"""

def solve(test):
  N,M,H,K=map(int,input().split())
  S=input()
  item=set([tuple(map(int,input().split())) for _ in range(M)])
  ans='Yes'
  x,y=0,0
  for i in range(N):
    H-=1
    if S[i]=='R': x+=1
    elif S[i]=='L': x-=1
    elif S[i]=='U': y+=1
    else: y-=1
    if H<0: ans='No'
    if (x,y) in item and H<K:
      item.remove((x,y))
      H=K
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)
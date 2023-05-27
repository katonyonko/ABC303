import io
import sys

_INPUT = """\
6
6
1 2
2 3
3 4
4 5
5 6
9
3 9
7 8
8 6
4 6
4 1
5 9
7 3
5 2
20
8 3
8 18
2 19
8 20
9 17
19 7
8 7
14 12
2 15
14 10
2 13
2 16
2 1
9 5
10 15
14 6
2 4
2 11
5 12
"""

def solve(test):
  N=int(input())
  G=[[] for _ in range(N)]
  for _ in range(N-1):
    u,v=map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)
  ans=[]
  tmp=[0]*N
  for i in range(N):
    if len(G[i])>2:
      ans.append(len(G[i]))
  n=(N-1-(sum(ans)+len(ans)-1))//3
  ans+=[2]*n
  ans.sort()
  if test==0:
    print(*ans)
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
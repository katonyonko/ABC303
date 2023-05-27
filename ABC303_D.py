import io
import sys

_INPUT = """\
6
1 3 3
AAaA
1 1 100
aAaAaA
1 2 4
aaAaAaaAAAAaAaaAaAAaaaAAAAA
"""

def solve(test):
  X,Y,Z=map(int,input().split())
  S=input()
  inf=10**20
  dp=[inf]*(2*(len(S)+1))
  def idx(i,j): return i*(len(S)+1)+j
  dp[idx(0,0)]=0
  dp[idx(1,0)]=Z
  for i in range(len(S)):
    if S[i]=='a':
      dp[idx(0,i+1)]=min(dp[idx(0,i+1)],dp[idx(0,i)]+X,dp[idx(1,i)]+Y+Z)
      dp[idx(1,i+1)]=min(dp[idx(1,i+1)],dp[idx(1,i)]+Y,dp[idx(0,i)]+X+Z)
    else:
      dp[idx(0,i+1)]=min(dp[idx(0,i+1)],dp[idx(0,i)]+Y,dp[idx(1,i)]+X+Z)
      dp[idx(1,i+1)]=min(dp[idx(1,i+1)],dp[idx(1,i)]+X,dp[idx(0,i)]+Y+Z)
  ans=min(dp[idx(0,len(S))],dp[idx(1,len(S))])
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
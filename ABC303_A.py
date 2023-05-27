import io
import sys

_INPUT = """\
6
3
l0w
1ow
3
abc
arc
4
nok0
n0ko
"""

def solve(test):
  N=int(input())
  S=input()
  T=input()
  ans='Yes'
  for i in range(N):
    x,y=S[i],T[i]
    if x!=y and ((x!='1' or y!='l') and (x!='l' or y!='1')) and ((x!='0' or y!='o') and (x!='o' or y!='0')): ans='No'
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
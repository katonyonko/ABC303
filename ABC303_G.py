import io
import sys

_INPUT = """\
6
2 20
2 2
5 1
10 200
1 21
1 1
1 1
8 4
30 1
3 1
10 2
8 1
9 1
4 4
1 20
2 1
"""

def solve(test):
  N,H=map(int,input().split())
  J=[list(map(int,input().split())) for _ in range(N)]
  J=[[J[i][0],J[i][1],J[i][0]*J[i][1]] for i in range(N)]
  J.sort(key=lambda x: x[2])
  def score(t,d,m,n):
    if t<=m: return d*t*(n-m)
    elif t<=n: return d*((m+(t-1))*(t-m)//2+t*(n-t))
    else: return d*((m+(n-1))*(n-m)//2)
  ans=[]
  t,d,td=J.pop()
  while len(J)>0:
    while len(J)>0 and J[-1][-1]<J[-1][0]*d:
      a,b,ab=J.pop()
    if len(J)>0:
      a,b,ab=J.pop()
      m=(ab-1)//d+1
      ans.append((t,d,td,m))
      t,d,td=a,b,ab
  ans.append((t,d,td,1))
  # print(ans)
  l,r=0,10**18+1
  while r-l>1:
    mid=(l+r)//2
    now=mid
    mm=0
    for i in range(len(ans)):
      t,d,td,m=ans[i]
      if now>m:
        # print(t,d,m,now,score(t,d,m,now))
        mm+=score(t,d,m,now)
        now=m
    # print(l,r,mm)
    if mm>=H: r=mid
    else: l=mid
  if test==0:
    print(r-1)
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
import sys
finput = sys.stdin.readline().rstrip()
repeatNum = int(finput)

def gcd(a,b):
  if(b>a) : a,b = b,a
  while(b!=0):
    a=a%b
    a,b=b,a
  return a

def L(a,b):
  print((a*b)//gcd(a,b))

for i in range(0, repeatNum):
  a,b = map(int, sys.stdin.readline().split())
  L(a,b)

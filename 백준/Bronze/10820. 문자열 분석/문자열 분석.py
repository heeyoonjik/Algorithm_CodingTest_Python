import sys
while(True):
  high, low, empty, num = 0, 0, 0, 0
  s = sys.stdin.readline().rstrip('\n')
  if not s:
    break
  for c in s:
    if(c.isalpha()):
      if(c.isupper()):
        high += 1
      else:
        low += 1
    elif(c == ' '):
        empty += 1
    else:
      num += 1
  print(low,high,num,empty)
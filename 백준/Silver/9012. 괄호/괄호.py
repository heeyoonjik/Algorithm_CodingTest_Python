import sys
input = sys.stdin.readline

for _ in range(int(input())):
  stack = []
  isVPS = 'YES'
  for psCharacter in input():
    if(psCharacter == '('):
      stack.append(psCharacter)
    elif(psCharacter == ')'):
      if stack:
        stack.pop()
      else:
        isVPS = 'NO'
  if stack:
    isVPS = 'NO'
  print(isVPS)
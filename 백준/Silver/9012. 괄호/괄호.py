repeatTime = int(input())

for _ in range(repeatTime):
  stack = []
  isVps = "YES"
  for inputCharacter in input():
    if(inputCharacter == '('):
      stack.append('(')
    elif(len(stack)<1):
      isVps = "NO"
    else:
      stack.pop()
  if stack:
    isVps = "NO"
  print(isVps)
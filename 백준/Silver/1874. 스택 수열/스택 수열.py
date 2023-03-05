import sys
input = sys.stdin.readline
repeatNumber = int(input())
sequenceStack = []
stack = []
result = []
for i in range(repeatNumber):
  sequenceStack.append(int(input().strip()))

sequenceStackIndex = 0
stackPushIndex = 0
whileIndex = 0
while True:
  if(whileIndex == 2*repeatNumber ):
    break
  if(len(stack) > 0 and stack[-1] == sequenceStack[sequenceStackIndex]):
      stack.pop()
      sequenceStackIndex += 1
      result.append('-')
  else:
      stack.append(stackPushIndex+1)
      result.append('+')
      stackPushIndex += 1
  whileIndex += 1

if stack:
  print('NO')
else:
  for i in result:
    print(i)
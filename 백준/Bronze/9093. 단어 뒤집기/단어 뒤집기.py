import sys
input = sys.stdin.readline

for _ in range(int(input())):
  inputSentence = input().split()
  for i in inputSentence:
    characterSet = list(i)
    stack = []
    for k in characterSet:
      stack.append(k)
    originalStackLength = len(stack)
    for _ in range(originalStackLength):
      print(stack.pop(), end="")
    print(end=" ")

import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
  inputValue = input().split()
  if(inputValue[0] == "push"):
    stack.append(inputValue[1])
  elif(inputValue[0] == "top"):
    if stack:
      print(stack[-1])
    else:
      print(-1)
  elif(inputValue[0] == "size"):
    print(len(stack))
  elif(inputValue[0] == "empty"):
    if stack:
      print(0)
    else:
      print(1)
  elif(inputValue[0] == "pop"):
    if stack:
      print(stack.pop())
    else:
      print(-1)
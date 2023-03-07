import sys
input = sys.stdin.readline

stackFront = list(input().strip())
stackBack = []

for _ in range(int(input())):
  command = list(input().strip())
  if command[0] == 'P':
    stackFront.append(command[2])
  elif command[0] == 'L':
    if stackFront:
      stackBack.append(stackFront.pop())
  elif command[0] == 'D':
    if stackBack:
      stackFront.append(stackBack.pop())
  elif command[0] == 'B':
    if stackFront:
      stackFront.pop()

print("".join(stackFront + list(reversed(stackBack))))
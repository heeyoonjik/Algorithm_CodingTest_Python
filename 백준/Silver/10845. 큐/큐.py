from sys import stdin
from collections import deque
queue = deque()
for _ in range(int(input())):
  inputLine = stdin.readline().split()
  cmd = inputLine[0]
  if cmd == "push":
    queue.append(int(inputLine[1]))
  elif cmd == "pop":
    print(queue.popleft() if len(queue) else -1)
  elif cmd == "front":
    print(queue[0] if len(queue) else -1)
  elif cmd == "back":
    print(queue[-1] if len(queue) else -1)
  elif cmd == "size":
    print(len(queue))
  elif cmd == "empty":
    print(0 if len(queue) else 1)

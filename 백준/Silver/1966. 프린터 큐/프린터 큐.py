from collections import deque

repeat = int(input())

def isBigger(queue):
  for i in queue:
    if(queue[0] < i):
      return True
  return False



for _ in range(repeat):
  num, index = map(int, input().split())
  queue = deque()
  for x in input().split():
    queue.append(x)
  current_index = index
  order = 1
  while True:
    if(isBigger(queue)):
      queue.append(queue.popleft())
      if(current_index == 0):
        current_index = len(queue) - 1
      else:
        current_index -= 1
    
    else:
      if(current_index == 0):
        break
      order += 1
      queue.popleft()
      current_index -= 1
      
  print(order)
from collections import deque

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  graph[x][y] = 0
  cnt = 0
  while queue:
    cnt += 1
    x,y = queue.popleft()

    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]
      if(0 <= dx < size and 0<= dy < size):
        if(graph[dx][dy] == '1'):
          queue.append((dx,dy))
          graph[dx][dy] = 0
  return cnt

size = int(input())
graph = [list(input()) for _ in range(size)]

mx = [1,-1,0,0]
my = [0,0,1,-1]
answer = []
total_cnt = 0

for i in range(size):
  for j in range(size):
    number = graph[i][j]
    if(number == '1'):
      answer.append(bfs(i,j))
      total_cnt += 1

print(total_cnt)
for i in sorted(answer):
  print(i)

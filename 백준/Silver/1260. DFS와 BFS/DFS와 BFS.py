from collections import deque

cmd = list(map(int,input().split()))
tree = [[0] * cmd[0] for _ in range(cmd[0])]
for _ in range(cmd[1]):
  x,y = map(int,input().split())
  tree[x-1][y-1] = 1
  tree[y-1][x-1] = 1
isVisited = [False] * cmd[0]
def dfs(nowNode):
  print(nowNode+1, end=" ")
  isVisited[nowNode] = True
  for nextNode in range(cmd[0]):
    if tree[nowNode][nextNode] and not isVisited[nextNode]:
      dfs(nextNode)

def bfs(firstNode):
  isBfsVisited = [False] * cmd[0]
  dq = deque()
  dq.append(firstNode)
  isBfsVisited[firstNode] = True
  while dq:
    nowNode = dq.popleft()
    print(nowNode+1, end=" ")
    for nextNode in range(cmd[0]):
      if tree[nowNode][nextNode] and not isBfsVisited[nextNode]:
        dq.append(nextNode)
        isBfsVisited[nextNode] = True

dfs(cmd[2]-1)
print()
bfs(cmd[2]-1)
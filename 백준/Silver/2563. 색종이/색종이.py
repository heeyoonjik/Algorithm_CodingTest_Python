# 100 x 전체 도형의 개수 에서 겹치는 면적을 빼면 되겠다고 처음 생각했으나,
# 도형의 개수와 겹치는 부분이 많아지면, 겹치는 면적을 구하기 어렵겠다고 생각했다.
# 따라서 100 x 100 이차원 리스트를 만들고, 거기에 1을 넣는 방식으로 색칠을 한 뒤,
# 전체 1의 개수를 구하는 방식으로 문제를 풀기로 했다.

paper_count = int(input())
pallet = [[0] * 100 for _ in range(100)]

for _ in range(paper_count):
  x,y = map(int, input().split())
  for i in range(10):
    for j in range(10):
      pallet[x+i][y+j] = 1

cnt = 0

for i in range(100):
  for j in range(100):
    if pallet[i][j] == 1:
      cnt += 1

print(cnt)
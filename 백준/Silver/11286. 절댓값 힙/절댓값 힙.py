import heapq as hq
import sys

input = sys.stdin.readline
pq = []

for _ in range(int(input())):
  inputNumber = int(input())
  if inputNumber:
    hq.heappush(pq, (abs(inputNumber), inputNumber))
  else:
    print(hq.heappop(pq)[1] if pq else 0)

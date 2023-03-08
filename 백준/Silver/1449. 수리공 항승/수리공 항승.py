import sys
input = sys.stdin.readline

coordinate = [False] * 1001

repeatNum, tapeLength = map(int, input().split())
for i in map(int, input().split()):
  coordinate[i] = True


index = 0
tapeCount = 0

while index <= 1000:
  if(coordinate[index]):
    tapeCount += 1
    index += tapeLength
  else:
    index += 1
print(tapeCount)
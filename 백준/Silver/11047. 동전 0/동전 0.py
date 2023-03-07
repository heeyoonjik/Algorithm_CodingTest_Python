import sys
input = sys.stdin.readline
repeatNumber,goalNumber = map(int, input().split())
unit = []
count = 0

for _ in range(repeatNumber):
  inputUnit = int(input())
  if(inputUnit>goalNumber):
    continue
  else:
    unit.append(inputUnit)

for divideNum in reversed(unit):
    count += int(goalNumber / divideNum)
    goalNumber %= divideNum

print(count)
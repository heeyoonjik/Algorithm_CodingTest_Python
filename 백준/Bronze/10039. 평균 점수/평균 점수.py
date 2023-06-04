sum = 0
for i in range(0, 5):
  newNum = int(input())
  if newNum > 40:
    sum += newNum
  else:
    sum += 40

print(sum // 5)
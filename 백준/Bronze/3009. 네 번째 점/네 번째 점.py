resultX = 0
resultY = 0
dicX = {}
dicY = {}
for i in range(3):
  x,y = map(int,input().split())
  if x in dicX:
    dicX[x] = dicX[x] + 1
  else:
    dicX[x] = 1
  if y in dicY:
    dicY[y] = dicY[y] + 1
  else:
    dicY[y] = 1

for key, value in dicX.items():
  if value <= 1:
    resultX = key
for key, value in dicY.items():
  if value <= 1:
    resultY = key

print(resultX,resultY)
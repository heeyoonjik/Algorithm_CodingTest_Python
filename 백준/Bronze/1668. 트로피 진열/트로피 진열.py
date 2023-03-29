trophyNum = int(input())
trophySize = []
for _ in range(trophyNum):
  trophySize.append(int(input()))

def judgment():
  answer = 0
  maxSize = 0
  for i in range(trophyNum):
    if(trophySize[i]>maxSize):
      maxSize = trophySize[i]
      answer +=1
    else:
      continue
  print(answer)

judgment()
trophySize.reverse()
judgment()

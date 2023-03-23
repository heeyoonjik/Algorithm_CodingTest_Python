def findMostAlcohole(numberOfUniversity):
  alcoholeDic = {}
  for _ in range(numberOfUniversity):
    inputlist = input().split()
    alcoholeDic[inputlist[0]] = int(inputlist[1])
  maxKey = max(alcoholeDic, key=alcoholeDic.get)
  print(maxKey)

for _ in range(int(input())):
  findMostAlcohole(int(input()))

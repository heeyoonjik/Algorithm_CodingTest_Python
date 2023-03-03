from itertools import combinations
dwarfHeight = []
for _ in range(9):
  dwarfHeight.append(int(input()))

for combinationTuple in combinations(dwarfHeight, 7):
  if(sum(combinationTuple) == 100):
    break
combinationTuple = sorted(combinationTuple)
for i in combinationTuple:
  print(i)
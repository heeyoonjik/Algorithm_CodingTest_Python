numbers = list(range(1, int(input())+1))
movingCMD = map(int,input().split())
for idx,val in enumerate(movingCMD):
  tmp = numbers[idx]
  del numbers[idx]
  numbers.insert(idx-val,tmp)
[print(i, end=" ") for i in numbers]
a, b = map(int, input().split())
bArr = list(str(b))
bNum = 0

def machineForList():
  num = ""
  for i in bArr:
    num += i
  return list(str(int(num)//2))

def machineForNum():
  num = ""
  for i in bArr:
    num += i
  return int(num)

index = 1
while True:
  if bArr[-1] == "1" :
    bArr.pop()
  elif machineForNum()%2 != 0:
    index = -1
    break
  else:
    tmp = machineForList()
    bArr.clear()
    bArr = tmp
  if(machineForNum() == a):
    index += 1
    break
  if(machineForNum() == 1):
    index = -1
    break
  index += 1

print(index)
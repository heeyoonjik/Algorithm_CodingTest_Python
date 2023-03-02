soldBookList = dict()

for _ in range(int(input())):
  inputBook = input()
  if(inputBook in soldBookList):
    soldBookList[inputBook] = soldBookList[inputBook] + 1
  else:
    soldBookList[inputBook] = 1
    
tmp = [k for k,v in soldBookList.items() if max(soldBookList.values()) == v]
tmp.sort()
print(tmp[0])
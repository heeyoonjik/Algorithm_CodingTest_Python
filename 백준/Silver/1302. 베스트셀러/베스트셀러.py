soldBooks = dict()

for _ in range(int(input())):
  bookname = input()
  if bookname in soldBooks:
    soldBooks[bookname] += 1
  else:
    soldBooks[bookname] = 1
  tmp = []

for k,v in soldBooks.items():
  if max(soldBooks.values()) == v:
    tmp.append(k)
tmp.sort()
print(tmp[0])
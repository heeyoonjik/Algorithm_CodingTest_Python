numberOfBasket, numberOfChanging = map(int, input().split())
arr = []
for i in range(1, numberOfBasket+1):
    arr.append(i)

for _ in range(numberOfChanging):
  a,b = map(int, input().split())
  tmp = arr[a-1]
  arr[a-1] = arr[b-1]
  arr[b-1] = tmp

for i in arr:
  print(i, end=" ")
price, count, account = map(int, input().split())
total = price * count
if(total > account):
  print(total - account)
else:
  print(0)
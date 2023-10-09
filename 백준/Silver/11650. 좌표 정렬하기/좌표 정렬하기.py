count = int(input())
li = []
for _ in range(count):
  a, b = (map(int, input().split()))
  li.append((a,b))

for i in sorted(li):
  print(i[0], i[1])
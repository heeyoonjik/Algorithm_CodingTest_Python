h, m, s = map(int, input().split())
time = int(input())
th = time//3600
time = time - th*3600
tm = time//60
ts = time%60
h += th
m += tm
s += ts
if(s>=60):
  m += 1
  s %= 60
if(m>=60):
  h += 1
  m %= 60
if(h>=24):
  h %= 24
print(h, m,s)
n = int(input())
originalN = n
count = 0
sibal = n//5
if(sibal==0 and n%3==0):
  count+=1
for i in range(sibal,0,-1):
  count = i
  n = originalN - i*5
  if(n%3 == 0):
    count += n//3
    n=0
    break
if n!=0:
  if originalN%3==0:
    count = originalN//3
  else:
    count = 0
print(count if count>0 else -1)

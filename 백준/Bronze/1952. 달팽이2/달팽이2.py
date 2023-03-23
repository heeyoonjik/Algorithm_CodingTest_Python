m,n = map(int, input().split())
answer = 0
while (m>=2 and n>=2):
  if m == 2:
    answer += 2
    break
  elif n == 2:
    answer += 3
    break
  else:
    answer += 4
  m -= 2
  n -= 2
  if (n == 1 and m!=1):
    answer += 1
    break

print(answer)

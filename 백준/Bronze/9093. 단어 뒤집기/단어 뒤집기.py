for _ in range(int(input())):
  word = input().split()
  for w in word:
    print(w[::-1], end=" ")
  print()

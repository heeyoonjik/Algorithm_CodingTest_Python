sizeOfNumbers, startNumber = map(int, input().split())

numbers = list(range(1, sizeOfNumbers+1))
answer = []
itemToRemoveIndex = startNumber-1
while len(numbers) > 0 :
  answer.append(numbers[itemToRemoveIndex])
  del numbers[itemToRemoveIndex]
  itemToRemoveIndex += startNumber-1
  while itemToRemoveIndex >= len(numbers) and len(numbers) != 0:
    itemToRemoveIndex -= len(numbers)

print("<", end="")
for i in answer:
  if i != answer[-1]:
    print(i, end=", ")
  else:
    print(i, end="")
print(">")

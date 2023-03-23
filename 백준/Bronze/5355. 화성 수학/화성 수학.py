for _ in range(int(input())):
  inputList = input().split()
  number = float(inputList[0])
  for i in range(1,len(inputList)):
    if inputList[i] == '@':
      number *= 3
    elif inputList[i] == '%' :
      number += 5
    else:
      number-= 7
  print(f"{number:.2f}")
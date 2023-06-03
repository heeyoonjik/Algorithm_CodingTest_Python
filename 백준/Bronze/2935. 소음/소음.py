import sys
num1 = int(sys.stdin.readline())
operator = sys.stdin.readline().rstrip()
num2 = int(sys.stdin.readline())
if operator == "+":
  print(num1 + num2)
else:
  print(num1 * num2)

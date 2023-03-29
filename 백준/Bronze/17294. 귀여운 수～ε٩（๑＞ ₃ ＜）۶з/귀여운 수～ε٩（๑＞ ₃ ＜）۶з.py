digits = [int(digit) for digit in input()]
answer = "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"
d = 0
if(len(digits)>=2):
  d = digits[1]-digits[0]
for idx in range(len(digits)-1):
  if(digits[idx+1]-digits[idx] != d):
    answer = "흥칫뿡!! <(￣ ﹌ ￣)>"
    break
print(answer)
n = int(input())
arr = map(int, input().split())
sorted_arr = sorted(arr)
max = int(input())
if(sum(sorted_arr)<=max):
  print(sorted_arr[-1])
elif sorted_arr[0]*n > max:
    print(int(max/n))
else:
  standardIndex = 0
  for idx, val in enumerate(sorted_arr):
    tmp_list = sorted_arr[:idx] + [val if x > val else x for x in sorted_arr[idx:]]
    if sum(tmp_list)>max:
      break
    standardIndex = idx
  for standardNumber in range(sorted_arr[standardIndex], sorted_arr[-1]):
    tmp_list = sorted_arr[:standardIndex] + [standardNumber if x > standardNumber else x for x in sorted_arr[standardIndex:]]
    if sum(tmp_list)>max:
      print(standardNumber-1)
      break

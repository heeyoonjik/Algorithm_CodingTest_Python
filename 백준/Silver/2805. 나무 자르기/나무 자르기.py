import sys
input = sys.stdin.readline
num_of_tree, sum_of_tree = map(int,input().split())
tree_list = list(map(int, input().split()))
start = 1
end = max(tree_list)

while start<=end:
  center = (start+end)//2
  total = 0
  
  for i in tree_list:
    if i>=center:
      total += i - center
    if(total>=sum_of_tree):
      break
  if total >= sum_of_tree:
    start = center + 1
  else:
    end = center - 1

print(end)
from itertools import combinations

n, standard_max = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()

data = list(combinations(num_list, 3))
max_sum = 0
for item in data:
  sum_of_tuple = sum(item)
  if sum_of_tuple>max_sum and sum_of_tuple<=standard_max:
    max_sum = sum_of_tuple

print(max_sum)
# 이장님 초대
# 백준 9237번

n = int(input())
days = list(map(int, input().split()))

days.sort(reverse=True)

max_days = days[0]

if n == 1:
    # print(n + 2)
    print(max_days + 2)
else:
    for i in range(1, n):
        if max_days < (i + days[i]):
            max_days = i + days[i]

    result = max_days + 2
    print(result)

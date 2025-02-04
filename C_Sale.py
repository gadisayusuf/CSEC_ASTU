n, m = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()

max_sum = 0
for i in range(m):
    if prices[i] < 0:
        max_sum -= prices[i] 
    else:
        break

print(max_sum)
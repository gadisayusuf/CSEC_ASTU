n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
def can_bake(x):
    total_powder_needed = 0
    for i in range(n):
        required = x * a[i]
        if required > b[i]:
            total_powder_needed += required - b[i]
        if total_powder_needed > k:
            return False
    return total_powder_needed <= k
left, right = 0, 10**9
while left < right:
    mid = (left + right + 1) // 2
    if can_bake(mid):
        left = mid
    else:
        right = mid - 1
print(left)
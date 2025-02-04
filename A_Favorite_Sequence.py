t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = []
    l, r = 0, n - 1
    while l <= r:
        if l == r:
            result.append(arr[l])
        else:
            result.append(arr[l])
            result.append(arr[r])
        l += 1
        r -= 1
    print(" ".join(map(str, result)))
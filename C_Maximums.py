n = int(input())
b = list(map(int, input().split()))
a = [0] * n
a[0] = b[0]
max_a = a[0]
for i in range(1, n):
    a[i] = b[i] + max_a
    max_a = max(max_a, a[i])
for i in a:
    print(i, end=" ")
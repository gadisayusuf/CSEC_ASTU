
s1, s2 = input().split()
n = int(input())
print(s1, s2)
for _ in range(n):
    a, b = input().split()
    if s1 == a:
        s1 = b
    elif s2 == a:
        s2 = b
    print(s1, s2)
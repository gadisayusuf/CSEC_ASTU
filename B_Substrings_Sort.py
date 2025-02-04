n=int(input())
s=[input().strip() for i in range(n)]
s.sort(key=len)
valid=True
for i in range(n-1):
    if s[i] not in s[i+1]:
        valid=False
        break
if valid:
    print('YES')
    for i in s:
        print(i)
else:
    print('NO')

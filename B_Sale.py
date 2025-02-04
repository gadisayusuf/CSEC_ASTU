# n,m=map(int,input().split())
# arr=list(map(int,input().split()))
# arr.sort()
# s=0
# for i in range(m):
#     s+=arr[i]
# print(abs(s))
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = 0
for i in range(m):
    if arr[i] < 0:
        s += arr[i]
print(abs(s))
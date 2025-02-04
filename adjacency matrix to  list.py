from collections import defaultdict
d=defaultdict(list)
n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(len(l)):
        d[i].append((j,l[j]))
print(d)
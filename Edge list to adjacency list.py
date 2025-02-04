from collections import defaultdict
n=int(input())
d=defaultdict(list)
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(1,n):
        d[l[0]].append(l[j])
for key,value in d.items():
    print(key,":",value)
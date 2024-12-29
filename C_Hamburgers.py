s=input()
nb,ns, nc=map(int,input().split())
pb,ps, pc=map(int,input().split())
r=int(input())
countb = s.count('B')
counts = s.count('S')
countc = s.count('C')
def can_make(x):
    needed_b = max(0, x * countb - nb)
    needed_s = max(0, x * counts - ns)
    needed_c = max(0, x * countc - nc)
    total_cost = needed_b * pb + needed_s * ps + needed_c * pc
    return total_cost <= r
left, right = 0, 10**13
while left < right:
    mid = (left + right + 1) // 2
    if can_make(mid):
        left = mid
    else:
        right = mid - 1
print(left)

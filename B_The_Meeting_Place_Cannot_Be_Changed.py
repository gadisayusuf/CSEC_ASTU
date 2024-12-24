n = int(input())
positions = list(map(int, input().split()))
speeds = list(map(int, input().split()))
def can_meet_in_time(t):
    min_pos = float('-inf')
    max_pos = float('inf')
    for i in range(n):
        min_pos = max(min_pos, positions[i] - speeds[i] * t)
        max_pos = min(max_pos, positions[i] + speeds[i] * t)
    return min_pos <= max_pos
left, right = 0, 10**9
while right - left > 1e-7:
    mid = (left + right) / 2
    if can_meet_in_time(mid):
        right = mid
    else:
        left = mid
print(right)
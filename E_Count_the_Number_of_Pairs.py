t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    lower_count = [0] * 26
    upper_count = [0] * 26
    for char in s:
        if char.islower():
            lower_count[ord(char) - ord('a')] += 1
        else:
            upper_count[ord(char) - ord('A')] += 1
    pairs = 0
    operations = 0
    for i in range(26):
        pairs += min(lower_count[i], upper_count[i])
        operations += abs(lower_count[i] - upper_count[i]) // 2
    pairs += min(operations, k)
    print(pairs)
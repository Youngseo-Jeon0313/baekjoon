def init(node, start, end):
    if start == end:
        tree[node] = 0
        return
    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)
    tree[node] = 0

def update(node, start, end, idx, val):
    if idx < start or end < idx:
        return
    if start == end:
        tree[node] += val
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, idx, val)
    update(node * 2 + 1, mid + 1, end, idx, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

n = int(input())
lines = []
for i in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
    lines.append((b, a))

lines.sort()
tree = [0] * (4 * n)

ans = 0
for i in range(2 * n):
    if i > 0 and lines[i][0] > lines[i - 1][0]:
        cnt = query(1, 0, 200000, 0, 200000)
        ans = max(ans, cnt)
    if lines[i][1] < 0:
        update(1, 0, 200000, -lines[i][1], -1)
    else:
        update(1, 0, 200000, lines[i][1], 1)

print(ans)

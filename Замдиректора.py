#Замдиректора
n, _ = map(int, input().split))
d = {1: 0}
for _ in range(n-1):
    x, y = map(int, input().split))
    d[y] = d[x]+1
print(d)
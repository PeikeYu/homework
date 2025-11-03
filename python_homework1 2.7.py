def joseph(n, m):
    p = 0
    for i in range(2, n+1):
        p = (p + m) % i
    return p + 1

n = 233
m = 3
print(joseph(n, m))
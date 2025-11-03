a, b = 0, 1
print(a, b, end=' ')
for _ in range(18):
    c = a + b
    print(c, end=' ')
    a, b = b, c
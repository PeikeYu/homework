count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i * 100 + j * 10 + k)
                count += 1
print(f"共有 {count} 个互不相同且无重复数字的三位数")
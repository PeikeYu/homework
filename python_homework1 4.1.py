import random
with open("data.txt", "w") as f:
    for _ in range(10):
        line = [random.randint(1, 100) for _ in range(3)]
        f.write(','.join(map(str, line)) + '\n')
with open("data.txt", "r") as f:
    column = []
    for line in f:
        column.append(int(line.split(',')[1]))
print("第二列最大值:", max(column))
print("第二列最小值:", min(column))
print("第二列平均值:", sum(column)/len(column))
print("第二列中位数:", sorted(column)[len(column)//2])
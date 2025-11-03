import random
import string
lines = int(input("请输入行数: "))
with open("test.txt", "w") as f:
    for _ in range(lines):
        f.write(''.join(random.choices(string.printable[:-5], k=10)) + '\n')
with open("test.txt", "rb") as src, open("copy_test.txt", "wb") as dst:
    dst.write(src.read())
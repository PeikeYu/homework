import os
import random
import string
os.makedirs("test", exist_ok=True)
num_files = int(input("请输入文件数量: "))
num_lines = int(input("请输入每行字符数: "))
for i in range(num_files):
    filename = f"file_{i}.txt"
    with open(f"test/{filename}", "w") as f:
        for _ in range(num_lines):
            f.write(''.join(random.choices(string.ascii_letters, k=10)) + '\n')
for filename in os.listdir("test"):
    new_name = filename.replace(".txt", "-python.txt")
    os.rename(f"test/{filename}", f"test/{new_name}")
    with open(f"test/{new_name}", "r") as f:
        content = f.read()
    with open(f"test/{new_name}", "w") as f:
        f.write(content.replace('\n', '=python\n'))
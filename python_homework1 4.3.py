with open("test.txt", "r") as f:
    content = f.read()
with open("test.txt", "w") as f:
    f.write("python" + content + "python")
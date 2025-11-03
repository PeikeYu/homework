import os
import random
files = os.listdir("img")
random.shuffle(files)
for file in files[:50]:
    if file.endswith(".png"):
        new_name = file[:-4] + ".jpg"
        os.rename(f"img/{file}", f"img/{new_name}")
import os
import string
import random
os.makedirs("img", exist_ok=True)
for i in range(100):
    filename = "".join(random.choices(string.ascii_uppercase + string.digits, k=4)) + ".png"
    with open(f"img/{filename}", "w") as f:
        pass
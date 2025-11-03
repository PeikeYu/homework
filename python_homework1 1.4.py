num = int(input("请输入一个正整数: "))
n = num
count = 0
while n > 0:
    n = n // 10
    count += 1
print(f"这是一个 {count} 位数")
n = num
print("逆序数字:", end=" ")
while n > 0:
    digit = n % 10
    print(digit, end=" ")
    n = n // 10
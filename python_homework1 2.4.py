num = int(input("请输入一个正整数: "))
n = num
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if rev == num:
    print(f"{num} 是回文数")
else:
    print(f"{num} 不是回文数")
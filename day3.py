import random
num = random.randint(1, 10)
i = 1
x = int(input(f"第{i}次机会，请输入："))
while x != num:
    if x > num:
        print("猜大了")
    else:
        print("猜小了")
    i += 1
    x = int(input(f"第{i}次机会，请输入："))
print(f"猜了{i}次终于猜对了，数字就是{num}！")

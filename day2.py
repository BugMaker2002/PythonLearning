num = 2
if num == int(input("请输入第一次猜想的数字：")):
    print("猜对了")
elif num == int(input("不对，再猜一次：")):
    print("猜对了")
elif num == int(input("不对，再猜最后一次：")):
    print("猜对了")
else:
    print(f"全猜错了，我猜的是{num}")


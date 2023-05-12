f = open("test.txt", "r", encoding="UTF-8")
print(f"f的类型是{type(f)}")
print(f"用read()函数读取10个字节的结果是：\n{f.read(10)}")
# 在程序中如果连续地调用read()函数，会从上一次读完的地方继续读取
print(f"用read()函数读取所有字节的结果是：\n{f.read()}")
f.close()

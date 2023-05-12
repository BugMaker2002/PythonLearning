import numpy as np
f = open("word.txt", "r", encoding="UTF-8")
content = f.readlines()
num = 0
for i in content:
    num += i.count("itheima")
print(num)
f.close()
a = np.arange(3)
print(a)

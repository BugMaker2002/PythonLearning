my_dict = {"Jack": 12, "Mark": 13, "Sherry": 14}
print("字典遍历方式一：")
for key in my_dict.keys():
    print(f"key:{key},values:{my_dict[key]}")
print("字典遍历方式二：")
for key in my_dict:
    print(f"key:{key},values:{my_dict[key]}")

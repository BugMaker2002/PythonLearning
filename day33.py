import os
# # 列出文件夹中的内容
# print(os.listdir("D:/AFile"))
# # 判断是不是文件夹
# print(os.path.isdir("D:/AFile"))
# # 判断是否存在该路径
# print(os.path.exists("D:/AFile"))
def get_file_from_recursion(path):
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + '/' + f
            if os.path.isdir(new_path):
                file_list += get_file_from_recursion(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}不存在")
        return []
    return file_list

print(get_file_from_recursion("D:/AFile"))

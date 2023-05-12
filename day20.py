import json
data1 = [{"name": "蔡徐坤", "age": 22}, {"name": "丁真", "age": 12}, {"name": "吴亦凡", "age": 11}]
data2 = {"name": "李易峰", "age": 30}
json1 = json.dumps(data1, ensure_ascii=False)
json2 = json.dumps(data2, ensure_ascii=False)
data3 = json.loads(json1)
data4 = json.loads(json2)
print(type(json1))
print(type(json2))
print(type(data3))
print(type(data4))


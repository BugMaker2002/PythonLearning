from typing import Union
import pyecharts
class Student:
    name = None
    age = None
    __phone = None

    def __str__(self):
        return f"name:{self.name},age:{self.age}"

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.__phone = phone

student = Student("丁真", 12, 1234)
print(student.age)

var1: int = 10
my_list: list[Union[int, str]] = [1, 2, "saa"]

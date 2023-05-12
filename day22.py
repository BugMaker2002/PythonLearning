class Student:

    def say(self):
        print(f"你好{self.name}")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("初始化完成")

student = Student("丁真", 21)
print(student.name)
print(student.age)
student.say()


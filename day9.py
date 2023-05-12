t1 = ("Python")
print(type(t1))
t2 = ("Python",)
print(type(t2))
t3 = ("Python", "Java", "C++", ["Jack", "Tom"])
print(t3)
t3[-1][0] = "Mark"
t3[-1][1] = "Shark"
print(t3)


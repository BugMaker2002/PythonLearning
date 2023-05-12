def out(func):
    def inner():
        print("开始")
        func()
        print("结束")
    return inner

@out
def sleep():
    print("在睡觉中")

sleep()



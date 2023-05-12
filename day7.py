num = 100
def tA():
    print(num)
def tB():
    tA()
    global num
    num = 200
    print(num)
def tC():
    return 1, True, "Hello"
# tA()
if __name__ == '__main__':
    tB()

# x, y, z = tC()
# print(x)
# print(y)
# print(z)
# print(num)

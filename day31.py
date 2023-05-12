import threading
import time
import re
def sing():
    while True:
        print("唱歌")
        time.sleep(1)
def dance():
    while True:
        print("跳舞")
        time.sleep(1)

if __name__ == '__main__':
    s_thread = threading.Thread(target=sing)
    d_thread = threading.Thread(target=dance)
    s_thread.start()
    d_thread.start()

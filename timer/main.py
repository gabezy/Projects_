from datetime import datetime
from time import sleep

def get_time():
    time = str(datetime.now().hour)+':'+str(datetime.now().minute)+':'+str(datetime.now().second)
    return time

def timer():
    while True:
        timer_ = get_time()
        print(timer_)
        sleep(1)


if __name__ == '__main__':
    print(timer())
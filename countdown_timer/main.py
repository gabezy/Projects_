from time import sleep
def countdonw(hour=1, min=0, sec=59):
    while hour > 0 or min > 0 or sec > 0:
        print(f'{display(hour)}:{display(min)}:{display(sec)}')
        sleep(1)
        
        if hour > 0 and min == 0 and sec == 0:
            hour -= 1
            min = 59
            sec = 59


        elif min > 0 and sec == 0:
            min -= 1
            sec = 59


        elif (min > 0 and sec > 0) or (min == 0 and sec > 0):
            sec -= 1
    
    print(f'{display(hour)}:{display(min)}:{display(sec)}')

        

def display(number):
    if number < 10:
        return f'0{number}'
    return f'{number}'


def fn(time):
    if time > 0:
        return 1
    elif time == 0:
        return 2




if __name__ == '__main__':
    countdonw()

